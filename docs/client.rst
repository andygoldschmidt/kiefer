Client
======

Before you start using the client, make sure you have a valid access token. If you don't have one yet, see :doc:`auth` for details.

The first step is to initialize the client with your access token:

::

  from kiefer.client import KieferClient

  client = KieferClient('YOUR_ACCESS_TOKEN')

The client provides endpoints for these event types:

-  band events
-  body events
-  heart rate
-  custom events
-  goals
-  meals
-  moods
-  moves
-  settings
-  sleeps
-  time zone
-  user information
-  workouts

Usage
-----

*kiefer* supports most of the endpoints provided by the `Jawbone UP API`_. The usage is straight forward:

::

  # Get information about authorized user
  client.get_user_information()

  # Add a new body event (weight)
  client.add_body_event(title='New body event', weight=85.0, body_fat=22.5, share=True)

  # Delete a sleep event
  client.delete_sleep('sleep_id')

  # Some endpoints support updates as well, e.g. workouts:
  client.update_workout('workout_id', calories=500)

For a full list of supported endpoints, please refer to the :doc:`api`.

Why do I get an authorization_error?
------------------------------------

You only can use endpoints that are covered by the scope of your access token. If you need more rights, change your scopes accordingly and request a new access token.

.. _Jawbone UP API: https://jawbone.com/up/developer/endpoints
