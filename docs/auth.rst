Authentication
==============

The UP API offers OAuth2 authentification, which requires user interaction to allow access of third-party services. `kiefer` aims to make this process as easy as possible.

Before we can start with the authentication process, we need to create a JSON config file. This config needs values for the following keys:

- :class:`client_id`
- :class:`client_secret`
- :class:`redirect_uri`
- :class:`scope`

For a list of available scopes have a look at `Jawbone's authentication docs`_. 

.. note::
  You can find a config file template here_.

After creating the config we can start authentication:

::

  from kiefer.auth import KieferAuth

  auth = KieferAuth('PATH_TO_CONFIG_FILE')
  access_token = auth.get_token()

.. _here: https://github.com/andygoldschmidt/kiefer/blob/master/config_example.json

.. _Jawbone's authentication docs: https://jawbone.com/up/developer/authentication
