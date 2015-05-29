Authentication
==============

The UP API offers OAuth2 authentification, which requires user interaction to allow access of third-party services. `kiefer` aims to make this process as easy as possible.

Before you start, go to the `Jawbone developer page`_ and create an account and an app, if you haven't done yet. Be sure to use an HTTPS *Redirect URI*.

Before we can start with the authentication process, we need to create a JSON config file. This config needs values for the following keys:

- :class:`client_id`
- :class:`client_secret`
- :class:`redirect_uri`
- :class:`scope`

You can copy the ``client_id`` and ``client_secret`` from your app page. For a list of available scopes have a look at `Jawbone's authentication docs`_. 

.. note::
  You can find a config file template here_.

After creating the config we can start authentication:

::

  from kiefer.auth import KieferAuth

  auth = KieferAuth('PATH_TO_CONFIG_FILE')
  access_token = auth.get_token()

When calling the ``get_token()`` method, you will be prompted to visit an authorization url. After permitting access copy and paste the **full redirect URL** into the command line prompt and your done.

Existing access token
---------------------

If you already have a valid access token, you can skip the whole authentication process and use the ``KieferClient`` directly.

Storing the access token
------------------------

Although there is no option to save the access token yet, you can put it in your config file and ``KieferAuth`` will recognize it during initialization:

::

  from kiefer.auth import KieferAuth

  access_token = KieferAuth('PATH_TO_CONFIG_FILE').access_token


.. _Jawbone developer page: https://jawbone.com/up/developer/
.. _here: https://github.com/andygoldschmidt/kiefer/blob/master/config_example.json
.. _Jawbone's authentication docs: https://jawbone.com/up/developer/authentication
