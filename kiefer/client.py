import requests


class KieferClientError(Exception):
    pass


class KieferClient(object):

    BASE_URL = 'https://jawbone.com/nudge/api/v.1.1/'

    def __init__(self, access_token):
        """
        Client class for the Jawbone UP API.

        :param access_token: Your access token for the UP API.
        :return:
        """
        self.access_token = access_token

    def _get(self, url):
        req_url = self.BASE_URL + url
        headers = {'Authorization': 'Bearer {}'.format(self.access_token)}
        r = requests.get(req_url, headers=headers)
        if r.status_code != 200:
            error_type = r.json()['meta']['error_type']
            error_detail = r.json()['meta']['error_detail']
            raise KieferClientError('{}: {}'.format(error_type, error_detail))
        return r.json()

    def get_band_events(self):
        return self._get('users/@me/bandevents')

    def get_body_events(self):
        return self._get('users/@me/body_events')

    def get_body_event(self, xid):
        return self._get('body_events/' + xid)

    def get_heart_rates(self):
        return self._get('users/@me/heartrates')

    def get_custom_events(self):
        return self._get('users/@me/generic_events')

    def get_goals(self):
        return self._get('users/@me/goals')

    def get_meals(self):
        return self._get('users/@me/meals')

    def get_meal(self, xid):
        return self._get('meals/' + xid)

    def get_moods(self):
        return self._get('users/@me/mood')

    def get_mood(self, xid):
        return self._get('mood/' + xid)

    def get_moves(self):
        return self._get('users/@me/moves')

    def get_move(self, xid):
        return self._get('moves/' + xid)

    def get_settings(self):
        return self._get('users/@me/settings')

    def get_sleeps(self):
        return self._get('users/@me/sleeps')

    def get_sleep(self, xid):
        return self._get('sleeps/' + xid)

    def get_timezone(self):
        return self._get('users/@me/timezone')

    def get_trends(self):
        return self._get('users/@me/trends')

    def get_user_information(self):
        return self._get('users/@me')

    def get_user_friends(self):
        return self._get('users/@me/friends')

    def get_workouts(self):
        return self._get('users/@me/workouts')

    def get_workout(self, xid):
        return self._get('workouts/' + xid)
