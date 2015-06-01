import json
import os

from requests_oauthlib import OAuth2Session
import requests
import sys
from kiefer.util import validate_response


def _get_input(msg):
    return input(msg) if sys.version_info.major == 3 else raw_input(msg)


class KieferAuthError(Exception):
    pass


class KieferAuth(object):
    """
    Takes care of authentication with the Jawbone UP API.
    The provided config file needs to include these 4 values:

    - ``client_id``
    - ``client_secret``
    - ``redirect_uri``
    - ``scope``

    Additionally, ``access_token`` and ``refresh_token`` will be recognized
    during initialization, if provided. This is helpful to retrieve the
    refresh token or to refresh your access token.

    :param config_path: :class:`str`, path to config file.
    """
    # Don't check scopes after retrieving token, UP API returns no scopes
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    _BASE_URL = 'https://jawbone.com/'
    _authorization_url = _BASE_URL + 'auth/oauth2/auth'
    _token_url = _BASE_URL + 'auth/oauth2/token'
    _refresh_token_url = _BASE_URL + '/nudge/api/v.1.1/users/@me/refreshToken'

    def __init__(self, config_path):
        if not os.path.isfile(config_path):
            raise IOError("No such file '{}'".format(config_path))

        self._config = json.load(open(config_path))
        self.client_id = self._config['client_id']
        self.client_secret = self._config['client_secret']
        self.redirect_uri = self._config['redirect_uri']
        self.scope = self._config['scope']
        if 'access_token' in self._config:
            self.access_token = self._config['access_token']
        if 'refresh_token' in self._config:
            self.refresh_token = self._config['refresh_token']

    def _create_session(self):
        return OAuth2Session(client_id=self.client_id,
                             redirect_uri=self.redirect_uri,
                             scope=self.scope)

    def _get_token(self, session, auth_response):
        return session.fetch_token(self._token_url,
                                   authorization_response=auth_response,
                                   client_secret=self.client_secret,
                                   method='GET')

    def get_access_token(self):
        """
        Use this method to retrieve your access token.

        :return: access_token
        """
        session = self._create_session()
        auth_url, state = session.authorization_url(self._authorization_url)

        print('Please go to this URL and grant access: {}'.format(auth_url))
        auth_response = _get_input('Please enter the full callback URL: ')
        token = self._get_token(session, auth_response)
        self.access_token = token['access_token']
        self.refresh_token = token['refresh_token']
        return self.access_token, self.refresh_token

    def set_access_token(self, token):
        """
        Set access token.

        :param token: :class:`str`
        """
        self.access_token = token

    def get_refresh_token(self):
        """
        Get refresh token.

        :return: refresh token
        """
        if not self.access_token:
            raise KieferAuthError('No access token available.')
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        payload = {'secret': self.client_secret}
        r = requests.post(self._refresh_token_url,
                          data=payload,
                          headers=headers)
        validate_response(r, 200, KieferAuthError)
        self.refresh_token = r.json()['data']['refresh_token']
        return self.refresh_token

    def set_refresh_token(self, token):
        """
        Set refresh token.

        :param token: :class:`str`
        """
        self.refresh_token = token

    def refresh_access_token(self):
        """
        Refresh your (expired) access token.

        The `KieferAuth` instance needs a valid access token and refresh token.
        Use :func:`set_access_token` and :func:`set_refresh_token` for that.
        Alternatively, you can add ``access_token`` and ``refresh_token`` as keys to your config file.

        :return: access token
        """
        payload = {'client_id': self.client_id,
                   'client_secret': self.client_secret}
        session = OAuth2Session(client_id=self.client_id)
        r = session.refresh_token(self._token_url, self.refresh_token, **payload)
        self.access_token = r['access_token']
        self.refresh_token = r['refresh_token']
        return self.access_token, self.refresh_token
