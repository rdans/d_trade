
#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import config

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

API_KEY_M_GAINER = config.API_KEY_MOST_GAINER
url = ("https://financialmodelingprep.com/api/v3/stock/gainers?apikey={}".format(API_KEY_M_GAINER))
# print(get_jsonparsed_data(url))
print(url)

