kiefer
======

.. image:: https://travis-ci.org/andygoldschmidt/kiefer.svg?branch=master

*Kiefer* (German): *jawbone*.

A simple Python wrapper for Jawbone's UP API. *kiefer* fully supports
Python 2.7 and Python 3.4.

Installation
------------

You can easily install *kiefer* using pip:

::

    pip install kiefer

Authentication
--------------

*kiefer* takes care of the tedious OAuth2 process.

Before you can start, you need to create a config file with your
``client_id``, ``client_secret``, ``redirect_uri`` and the ``scope`` of
your app. You can use the included ``config_example.json`` as a
template.

You can create your Jawbone account and app here:
`Link <https://jawbone.com/up/developer/account>`__

After creating the config file all interaction that is needed is
copy-pasting a URL:

::

    from kiefer.auth import KieferAuth

    auth = KieferAuth('config.json')
    access_token = auth.get_access_token()

Usage
-----

After retrieving your access token, initialize the client:

::

    from kiefer.client import KieferClient

    client = KieferClient(your_access_token)

A ``KieferClient`` instance offers endpoints for these event types:

-  band events
-  body event(s)
-  heart rate
-  custom events
-  goals
-  meal(s)
-  mood(s)
-  move(s)
-  settings
-  sleep(s)
-  time zone
-  user information
-  workout(s)

The usage is straight forward:

::

  # Get information about authorized user
  client.get_user_information()

  # Add a new body event (weight)
  client.add_body_event(title='New body event', weight=85.0, body_fat=22.5, share=True)

  # Delete a sleep event
  client.delete_sleep('sleep_id')

  # Some endpoints support updates as well, e.g. workouts:
  client.update_workout('workout_id', calories=500)
