import requests


class KieferClientError(Exception):
    pass


class KieferClient(object):
    """
    Client class for the Jawbone UP API.

    :param access_token: Your access token for the UP API.
    """
    BASE_URL = 'https://jawbone.com/nudge/api/v.1.1/'

    def __init__(self, access_token):
        self.access_token = access_token
        self._headers = {'Authorization': 'Bearer {}'.format(self.access_token)}

    # Endpoint implementation

    def get_band_events(self):
        """Get list of band hardware events."""
        return self._get('users/@me/bandevents')

    def get_body_events(self):
        """Get list of body events."""
        return self._get('users/@me/body_events')

    def get_body_event(self, xid):
        """
        Get a single body event.

        :param xid: :class:`str`, id of body event
        """
        return self._get('body_events/' + xid)

    def add_body_event(self, **kwargs):
        """
        Add body event (weight).

        Values for `**kwargs`:

        - title: string
        - weight: float (required)
        - body_fat: float
        - lean_mass: float
        - bmi: float
        - note: string
        - time_created: int
        - tz: string
        - share: bool

        :param kwargs: Parameters of body event
        """
        if 'weight' not in kwargs:
            raise KieferClientError("Required parameter 'weight' not found.")
        return self._post('users/@me/body_events', kwargs)

    def get_heart_rates(self):
        """Get list of heart rates."""
        return self._get('users/@me/heartrates')

    def get_custom_events(self):
        """Get list of custom/generic events."""
        return self._get('users/@me/generic_events')

    def get_goals(self):
        """Get list of goals."""
        return self._get('users/@me/goals')

    def get_meals(self):
        """Get list of meals."""
        return self._get('users/@me/meals')

    def get_meal(self, xid):
        """
        Get a single meal.

        :param xid: :class:`str`, id of meal
        """
        return self._get('meals/' + xid)

    def get_moods(self):
        """Get list of moods."""
        return self._get('users/@me/mood')

    def get_mood(self, xid):
        """
        Get a single mood.

        :param xid: :class:`str`, id of mood
        """
        return self._get('mood/' + xid)

    def get_moves(self):
        """Get list of moves."""
        return self._get('users/@me/moves')

    def get_move(self, xid):
        """
        Get a single move.

        :param xid: :class:`str`, id of move
        """
        return self._get('moves/' + xid)

    def get_settings(self):
        """Retrieve user settings."""
        return self._get('users/@me/settings')

    def get_sleeps(self):
        """Get list of sleeps."""
        return self._get('users/@me/sleeps')

    def get_sleep(self, xid):
        """
        Get a single sleep.

        :param xid: :class:`str`, id of sleep
        """
        return self._get('sleeps/' + xid)

    def get_timezone(self):
        """Get user time zone."""
        return self._get('users/@me/timezone')

    def get_trends(self):
        """Get trends."""
        return self._get('users/@me/trends')

    def get_user_information(self):
        """Get basic information of the user."""
        return self._get('users/@me')

    def get_user_friends(self):
        """Get list of the user's friends."""
        return self._get('users/@me/friends')

    def get_workouts(self):
        """Get list of workouts."""
        return self._get('users/@me/workouts')

    def get_workout(self, xid):
        """
        Get a single workout.

        :param xid: :class:`str`, id of workout
        """
        return self._get('workouts/' + xid)

    # Request helper methods

    def _get(self, endpoint):
        req_url = self.BASE_URL + endpoint
        r = requests.get(req_url, headers=self._headers)
        self._validate_response(r, 200)
        return r.json()

    def _post(self, endpoint, payload):
        req_url = self.BASE_URL + endpoint
        r = requests.post(req_url, headers=self._headers, data=payload)
        self._validate_response(r, 201)
        return r.json()

    @staticmethod
    def _validate_response(req, expected_status):
        if req.status_code != expected_status:
            error_type = req.json()['meta']['error_type']
            error_detail = req.json()['meta']['error_detail']
            raise KieferClientError('{}: {}'.format(error_type, error_detail))
        return True
