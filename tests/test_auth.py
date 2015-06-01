import os
import pytest
from kiefer.auth import KieferAuth


def test_auth_init_env_vars_set():
    auth = KieferAuth('tests/testconfig.json')
    assert os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] == '1'


def test_auth_init_attributes_set():
    auth = KieferAuth('tests/testconfig.json')
    for attr in ('client_id', 'client_secret', 'redirect_uri', 'scope'):
        assert attr in auth._config


def test_auth_init_fails_without_config():
    with pytest.raises(IOError):
        KieferAuth('noconfig.json')


def test_auth_get_access_token(mocker):
    input_mock = mocker.patch('kiefer.auth._get_input')
    token_mock = mocker.patch('requests_oauthlib.OAuth2Session.fetch_token')
    token_mock.return_value = {'access_token': 'access',
                               'refresh_token': 'refresh'}
    auth = KieferAuth('tests/testconfig.json')
    access_token, refresh_token = auth.get_access_token()
    input_mock.assert_called_once_with('Please enter the full callback URL: ')
    assert token_mock.call_count == 1
    assert access_token == auth.access_token == 'access'
    assert refresh_token == auth.refresh_token == 'refresh'


def test_auth_set_access_token():
    auth = KieferAuth('tests/testconfig.json')
    auth.set_access_token('abc')
    assert auth.access_token == 'abc'


def test_auth_set_refresh_token():
    auth = KieferAuth('tests/testconfig.json')
    auth.set_refresh_token('abc')
    assert auth.refresh_token == 'abc'
