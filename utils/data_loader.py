import json

def load_test_data():

    with open("config/test_data.json") as file:
        data = json.load(file)

    return data