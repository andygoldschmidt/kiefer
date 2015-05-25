# kiefer

*kiefer* (German):  *jawbone*.

A simple Python wrapper for Jawbone's UP API.  *kiefer* fully supports Python 2.7 and Python 3.4.

## Authentication

*kiefer* takes care of the tedious OAuth2 process. All you need to do is copy-pasting a URL:

```
from kiefer.auth import KieferAuth

auth = KieferAuth('config.json')
access_token = auth.get_token()
```

## Usage

After retrieving your access token, initialize the client:

```
from kiefer.client import KieferClient

client = KieferClient(your_access_token)
```

A `KieferClient` instance offers methods to retrieve following metrics from the Jawbone UP API:

* band events
* body event(s)
* heart rate
* custom events
* goals
* meal(s)
* mood(s)
* move(s)
* settings
* sleep(s)
* time zone
* user information
* workout(s)

A *(s)* indicates that you can retrieve a list of events as well as a single event.