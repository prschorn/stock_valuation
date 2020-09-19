import string
import json


def save_json(data, filename: string):
    file = open(filename, 'w')
    file.write(json.dumps(data, indent=4, sort_keys=True))
