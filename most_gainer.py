
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

# url = ("https://financialmodelingprep.com/api/v3/stock/gainers?apikey=547d8ef187922d70f8f9a1cbebd851c4")
# print(get_jsonparsed_data(url))
print(config.API_KEY_MOST_GAINER)

