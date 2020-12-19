#!/usr/bin/env python3
import requests
import os


if __name__ == '__main__':
    URL = "http://localhost/upload"
    IMG_DIR = os.path.join(os.path.expanduser("~"), "supplier-data", "images")
    for image in os.listdir(IMG_DIR):
        with open(os.path.join(IMG_DIR, image), 'rb') as opened:
            response = requests.post(URL, files={'file': opened})
            response.raise_for_status()