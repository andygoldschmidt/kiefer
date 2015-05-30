Authentication
==============

The UP API offers OAuth 2.0 authentification, which requires user interaction to allow access of third-party services. `kiefer` aims to make this process as easy as possible.

Before you start, go to the `Jawbone developer page`_ and create an account and an app, if you haven't done yet. Be sure to use an HTTPS *Redirect URI*.

Getting the access token
------------------------

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
  access_token, refresh_token = auth.get_access_token()

When calling the ``get_access_token()`` method, you will be prompted to visit an authorization url. After permitting access copy-paste the **full redirect URL** into the command line prompt and you're done.

Your access token and a refresh token are returned. The refresh token is needed to issue a new access token to you, when it expires.

Refreshing the access token
---------------------------

Currently, UP API access tokens are valid for 1 year. After that time, the token expires and you need to get a new one using your refresh token.

If you have a valid access token and forgot your refresh token, you can retrieve it using:

::

  refresh_token = auth.get_refresh_token()

After your access token is expired you can issue a new one like that:

::

  access_token, refresh_token = auth.refresh_access_token()

.. note::
  The ``KieferAuth`` object needs to have a valid refresh token set. You can either put the refresh token in your config (see :ref:`storing-tokens`) or you can set the it using the ``set_refresh_token()`` method.

Existing access token
---------------------

If you already have a valid access token, you can skip the whole authentication process and use the :doc:`client` directly.

.. _storing-tokens:

Storing tokens
--------------

Although there is no option to save the access token and refresh token yet, you can put them in your config file and ``KieferAuth`` will recognize them during initialization:

::

  from kiefer.auth import KieferAuth

  auth = KieferAuth('PATH_TO_CONFIG_FILE')
  access_token = auth.access_token
  refresh_token = auth.refresh_token


.. _Jawbone developer page: https://jawbone.com/up/developer/
.. _here: https://github.com/andygoldschmidt/kiefer/blob/master/config_example.json
.. _Jawbone's authentication docs: https://jawbone.com/up/developer/authentication
