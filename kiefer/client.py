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

    # Band events
    def get_band_events(self):
        """Get list of band hardware events."""
        return self._get('users/@me/bandevents')

    # Body events
    def get_body_events(self, **kwargs):
        """Get list of body events."""
        return self._get('users/@me/body_events', payload=kwargs)

    def get_body_event(self, xid):
        """
        Get a single body event.

        :param xid: ``str``, id of body event
        """
        return self._get('body_events/' + xid)

    def add_body_event(self, **kwargs):
        """
        Add body event (weight).

        Values for `**kwargs`:

        - title: ``str``
        - weight: ``float`` (required)
        - body_fat: ``float``
        - lean_mass: `float``
        - bmi: ``float``
        - note: ``str``
        - time_created: ``int``
        - tz: ``str``
        - share: ``bool``
        """
        if 'weight' not in kwargs:
            raise KieferClientError("Required parameter 'weight' not found.")
        return self._post('users/@me/body_events', kwargs)

    def delete_body_event(self, xid):
        """
        Delete a body event.

        :param xid: ``str``, id of body event
        """
        return self._delete('body_events/' + xid)

    # Heart rate
    def get_heart_rates(self, **kwargs):
        """Get list of heart rates."""
        return self._get('users/@me/heartrates', kwargs)

    def get_custom_events(self, **kwargs):
        """Get list of custom/generic events."""
        return self._get('users/@me/generic_events', kwargs)

    # Goals
    def get_goals(self):
        """Get list of goals."""
        return self._get('users/@me/goals')

    def update_goal(self, **kwargs):
        """
        Creates or updates an user's goal(s).

        Possible values for kwargs are:

        - move_steps: ``int``
        - sleep_total: ``int``
        - body_weight: ``float``
        - body_weight_intent: ``int`` (``0`` = lose, ``1`` = maintain, ``2`` = gain)
        """
        return self._post('/users/@me/goals', kwargs)

    # Meals
    def get_meals(self, **kwargs):
        """Get list of meals."""
        return self._get('users/@me/meals', kwargs)

    def get_meal(self, xid):
        """
        Get a single meal.

        :param xid: ``str``, meal id
        """
        return self._get('meals/' + xid)

    def add_meal(self, **kwargs):
        """
        Add a new meal.

        Possible values for kwargs are:

        - note: ``str``
        - sub_type: ``int`` (``1`` = Breakfast, ``2`` = Lunch, ``3`` = Dinner)
        - place_lat: ``float``
        - place_lon: ``float``
        - place_acc: ``float``
        - place_name: ``str``
        - time_created: ``int``
        - tz: ``str``
        - items: ``dict`` (For details refer to: https://jawbone.com/up/developer/endpoints/meals#post_meal)
        """
        return self._post('/users/@me/meals', kwargs)

    def update_meal(self, xid, **kwargs):
        """
        Updates an existing meal.

        Refer to :func:`add_meal` for a list of keyword arguments.

        :param xid: ``str``, id of meal
        """
        return self._post('/meals/{}/partialUpdate'.format(xid), kwargs)

    def delete_meal(self, xid):
        """
        Delete a meal.

        :param xid: ``str``, meal id
        """
        return self._delete('/meals/' + xid)

    # Moods
    def get_moods(self, **kwargs):
        """Get list of moods."""
        return self._get('users/@me/mood', kwargs)

    def get_mood(self, xid):
        """
        Get a single mood.

        :param xid: ``str``, id of mood
        """
        return self._get('mood/' + xid)

    def add_mood(self, **kwargs):
        """
        Add a new mood.

        Possible values for kwargs are:

        - title: ``str``
        - sub_type: ``int`` (``1`` = Amazing, ``2`` = Pumped UP, ``3`` = Energized, \
         ``8`` = Good, ``4`` = Meh, ``5`` = Dragging, ``6`` = Exhausted, ``7`` = Totally Done)
        - time_created: ``int``
        - tz: ``str``
        - share: ``bool``
        """
        return self._post('/users/@me/mood', kwargs)

    def delete_mood(self, xid):
        """
        Delete a mood.

        :param xid: ``str``, mood id
        """
        return self._delete('/mood/' + xid)

    # Moves
    def get_moves(self, **kwargs):
        """Get list of moves."""
        return self._get('users/@me/moves', kwargs)

    def get_move(self, xid):
        """
        Get a single move.

        :param xid: ``str``, move id
        """
        return self._get('moves/' + xid)

    def get_move_graph(self, xid):
        """
        Get graph of a single move.

        :param xid: ``str``, move id
        """
        return self._get('/moves/{}/image'.format(xid))

    def get_move_ticks(self, xid):
        """
        Get ticks of a single move.

        :param xid: ``str``, move id
        """
        return self._get('/moves/{}/ticks'.format(xid))

    # Settings
    def get_settings(self):
        """Retrieve user settings."""
        return self._get('users/@me/settings')

    # Sleeps
    def get_sleeps(self, **kwargs):
        """Get list of sleeps."""
        return self._get('users/@me/sleeps', kwargs)

    def get_sleep(self, xid):
        """
        Get a single sleep.

        :param xid: :class:`str`, id of sleep
        """
        return self._get('sleeps/' + xid)

    def get_sleep_graph(self, xid):
        """
        Get graph of a single sleep.

        :param xid: ``str``, sleep id
        """
        return self._get('/sleeps/{}/image'.format(xid))

    def get_sleep_phases(self, xid):
        """
        Get sleep phases of a single sleep.

        :param xid: ``str``, sleep id
        """
        return self._get('/sleeps/{}/ticks'.format(xid))

    def add_sleep(self, **kwargs):
        """
        Add a new sleep.

        Possible values for kwargs are:

        - time_created: ``int``
        - time_completed: ``int``
        - tz: ``str``
        - share: ``bool``
        """
        self._post('/users/@me/sleeps', kwargs)

    def delete_sleep(self, xid):
        """
        Delete a sleep.

        :param xid: ``str``, sleep id
        """
        self._delete('/sleeps/' + xid)

    # Timezone
    def get_timezone(self, **kwargs):
        """Get user time zone."""
        return self._get('users/@me/timezone', kwargs)

    # Trends
    def get_trends(self, **kwargs):
        """Get trends."""
        return self._get('users/@me/trends', kwargs)

    # User information
    def get_user_information(self):
        """Get basic information of the user."""
        return self._get('users/@me')

    def get_user_friends(self):
        """Get list of the user's friends."""
        return self._get('users/@me/friends')

    # Workouts
    def get_workouts(self, **kwargs):
        """Get list of workouts."""
        return self._get('users/@me/workouts', kwargs)

    def get_workout(self, xid):
        """
        Get a single workout.

        :param xid: :class:`str`, id of workout
        """
        return self._get('workouts/' + xid)

    def get_workout_graph(self, xid):
        """
        Get graph for a single workout.

        :param xid: ``str``, workout id
        """
        return self._get('/workouts/{}/image'.format(xid))

    def get_workout_ticks(self, xid):
        """
        Get ticks for a single workout.

        :param xid: ``str``, workout id
        """
        return self._get('/workouts/{}/ticks'.format(xid))

    def add_workout(self, **kwargs):
        """
        Add a new workout.

        Possible values for kwargs are:

        - sub_type: ``int`` (refer to https://jawbone.com/up/developer/endpoints/workouts#post_workout for list of values)
        - time_created: ``int``
        - time_completed: ``int``
        - place_lat: ``float``
        - place_lon: ``float``
        - place_acc: ``float``
        - place_name: ``str``
        - tz: ``str``
        - share: ``bool``
        - calories: ``int``
        - distance: ``int``
        - image_url: ``str``
        - intensity: ``int`` (``1`` = easy, ``2`` = moderate, ``3`` = intermediate, ``4`` = difficult, ``5`` = hard)
        """
        return self._post('/users/@me/workouts', kwargs)

    def update_workout(self, xid, **kwargs):
        """
        Updates an existing workout.

        Refer to :func:`add_workout` for a list of keyword arguments.

        :param xid: ``str``, workout id
        """
        self._post('/workouts/{}/partialUpdate'.format(xid), kwargs)

    def delete_workout(self, xid):
        """
        Delete a workout.

        :param xid: ``str, workout id
        """
        self._delete('/workouts/' + xid)

    # Request helper methods

    def _get(self, endpoint, payload=None):
        req_url = self.BASE_URL + endpoint
        r = requests.get(req_url, headers=self._headers, params=payload)
        self._validate_response(r, 200)
        return r.json()

    def _post(self, endpoint, payload):
        req_url = self.BASE_URL + endpoint
        r = requests.post(req_url, headers=self._headers, data=payload)
        self._validate_response(r, 201)
        return r.json()

    def _delete(self, endpoint):
        req_url = self.BASE_URL + endpoint
        r = requests.delete(req_url, headers=self._headers)
        self._validate_response(r, 200)
        return r.json()

    @staticmethod
    def _validate_response(req, expected_status):
        if req.status_code != expected_status:
            error_type = req.json()['meta']['error_type']
            error_detail = req.json()['meta']['error_detail']
            raise KieferClientError('{}: {}'.format(error_type, error_detail))
        return True
