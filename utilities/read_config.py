import json


def read_configuration():
    with open("config/config.json", "r") as json_file:
        return json.load(json_file)
