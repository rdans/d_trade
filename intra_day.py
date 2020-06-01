# Run the json for those:

# this is for finmodel
from urllib.request import urlopen
import json
import time
from datetime import datetime
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

def write_to_json(data):
    """
    Receive data from API call, then write to file

    Parameters
    ----------
    data : dict

    Returns
    -------
    None
    """
    # Serializing json  
    json_object = json.dumps(data, indent = 4) 

    date = datetime.now()
    date_str = date.strftime("%y%m%d_%H%M")
  
    # Writing to sample.json 
    with open("./intraday_data/json/i_data_{0}_{1}.json".format(date_str, int(time.time())), "w") as outfile: 
        outfile.write(json_object)


# read JSON File and create a set of ticker to run individually
# TO-DO -> Read current date and run all of the JSON with current date manually

set_of_ticker = set()
list_of_json = ['most_gainer_200529_0853_1590767595.json', 
                'most_gainer_200529_1116_1590776210.json',
                'most_gainer_200529_1628_1590794884.json']

for json_file in list_of_json:
    # Opening JSON file 
    with open('./most_gainer_data/{}'.format(json_file), 'r') as openfile: 
    
        # Reading from json file 
        json_object = json.load(openfile) 

        # adding the file to a set
        for item in json_object['mostGainerStock']:
            set_of_ticker.add(item['ticker'])



API_KEY_INTRA_DAY = config.API_KEY_INTRA_DAY

# need to limit 5 calls per minute
counter = 0 
data_id = 0
data_dict = {}
for ticker in set_of_ticker:
    data_id = data_id + 1
    counter = counter + 1
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval=15min&apikey={1}".format(ticker, API_KEY_INTRA_DAY)

    if counter == 2:
        time.sleep(45)
        counter = 0 
    
    print('Requesting intraday data ({0}/{1})'.format(data_id, len(set_of_ticker)))
    # run the API
    data = get_jsonparsed_data(url)
    # create a dict
    data_dict[data_id] = data

# store to JSON
write_to_json(data_dict)
    