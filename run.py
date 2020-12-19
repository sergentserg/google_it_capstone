#!/usr/bin/env python3
import os
import requests


def to_json(fp):
    with open(fp, 'r') as f:
        name, weight, description = [field.strip() for field in f.readlines()]
    return {
        "name": name,
        "weight": int(weight.split()[0]),
        "image_name": os.path.basename(fp),
        "description": description
    }


if __name__ == '__main__':
    DESC_DIR = os.path.join(os.path.expanduser("~"), 'supplier-data', 'descriptions')
    # The IP must be replaced in the next line.
    URL = "http://127.0.0.1/fruits"
    for fn in os.listdir(DESC_DIR):
        abspath = os.path.join(DESC_DIR, fn)
        response = requests.post(URL, json=to_json(abspath))
