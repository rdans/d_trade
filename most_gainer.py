
#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import config
import time
from datetime import datetime


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

data = get_jsonparsed_data(url)

# Serializing json  
json_object = json.dumps(data, indent = 4) 

date = datetime.now()
date_str = date.strftime("%y%m%d_%H%M")
  
# Writing to sample.json 
with open("./most_gainer_data/most_gainer_{0}_{1}.json".format(date_str, int(time.time())), "w") as outfile: 
    outfile.write(json_object)



