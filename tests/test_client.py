import requests
import pytest
from kiefer.client import KieferClient, KieferClientError


@pytest.fixture
def setup(mocker):
    class Setup:
        resp = mocker.patch.object(requests.Response, '__init__')
        resp.status_code = 200
        resp.json = lambda: {'meta': {'error_type': 'CustomError',
                                      'error_detail': 'custom error detail'}}
        req_get = mocker.patch('requests.get')
        req_get.return_value = resp

        req_post = mocker.patch('requests.post')
        req_post.return_value = resp

        req_delete = mocker.patch('requests.delete')
        req_delete.return_value = resp

        client = KieferClient('access_token')
        headers = {'Authorization': 'Bearer access_token'}
    return Setup


def test_client_client_init():
    client = KieferClient('access_token')
    assert client.access_token == 'access_token'
    assert client._headers['Authorization'] == 'Bearer access_token'


def test_client_get_helper(setup):
    req_url = 'https://jawbone.com/nudge/api/v.1.1/myurl'
    setup.client._get('myurl')
    setup.req_get.assert_called_once_with(req_url, params=None,
                                          headers=setup.headers)

    setup.resp.status_code = 404
    with pytest.raises(KieferClientError):
        setup.client._get('myurl')


def test_client_post_helper(setup):
    req_url = 'https://jawbone.com/nudge/api/v.1.1/myurl'
    setup.client._post('myurl', payload={})
    setup.req_post.assert_called_once_with(req_url, data={},
                                           headers=setup.headers)

    setup.resp.status_code = 404
    with pytest.raises(KieferClientError):
        setup.client._post('myurl', payload={'foo': 'bar'})


def test_client_delete_helper(setup):
    req_url = 'https://jawbone.com/nudge/api/v.1.1/myurl'
    setup.client._delete('myurl')
    setup.req_delete.assert_called_once_with(req_url, headers=setup.headers)

    setup.resp.status_code = 404
    with pytest.raises(KieferClientError):
        setup.client._delete('myurl')


def test_client_get_band_events(setup):
    url = 'https://jawbone.com/nudge/api/v.1.1/users/@me/bandevents'
    setup.client.get_band_events()
    setup.req_get.assert_called_once_with(url, params=None,
                                          headers=setup.headers)


def test_client_get_body_events(setup):
    url = 'https://jawbone.com/nudge/api/v.1.1/users/@me/body_events'
    setup.client.get_body_events()
    setup.req_get.assert_called_once_with(url, params={},
                                          headers=setup.headers)
