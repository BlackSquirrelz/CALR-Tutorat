import json


# Saving JSON File in a spcified location
def save_json(data, file_name):
    """ Generic function to save dictionary data to a JSON file"""
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


# Getting JSON Data
def get_json(file_name):
    """ Generic function to retrieve data from JSON file"""
    with open(file_name) as f:
        data = json.load(f)
        return data
