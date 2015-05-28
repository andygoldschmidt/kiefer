import json
import os

from requests_oauthlib import OAuth2Session
import sys


class KieferAuth(object):
    """
    Takes care of authentication with the Jawbone UP API.

    :param config_path: Path to config file.
    """
    # Don't check scopes after retrieving token, API returns no scopes
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    _authorization_url = 'https://jawbone.com/auth/oauth2/auth'
    _token_url = 'https://jawbone.com/auth/oauth2/token'

    def __init__(self, config_path):
        if not os.path.isfile(config_path):
            raise IOError("No such file '{}'".format(config_path))

        self._config = json.load(open(config_path))
        self.client_id = self._config['client_id']
        self.client_secret = self._config['client_secret']
        self.redirect_uri = self._config['redirect_uri']
        self.scope = self._config['scope']
        if 'access_token' in self._config.keys():
            self.access_token = self._config['access_token']

    def _create_session(self):
        return OAuth2Session(client_id=self.client_id,
                             redirect_uri=self.redirect_uri,
                             scope=self.scope)

    def _get_token(self, session, auth_response):
        return session.fetch_token(self._token_url, authorization_response=auth_response,
                                   client_secret=self.client_secret, method='GET')

    def get_token(self):
        """
        Use this method to retrieve your access token.

        :return: access_token
        """
        session = self._create_session()
        auth_url, state = session.authorization_url(self._authorization_url)

        print('Please go to this URL and grant access: {}'.format(auth_url))
        if sys.version_info.major == 3:
            auth_response = input('Please enter the full callback URL: ')
        else:
            auth_response = raw_input('Please enter the full callback URL: ')
        token = self._get_token(session, auth_response)
        self.access_token = token['access_token']
        return self.access_token
