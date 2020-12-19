#!/usr/bin/env python3
import os
from PIL import Image


RESOLUTION = (600, 400)


def process_images(img_dir):
    for infile in os.listdir(img_dir):
        name, _ = os.path.splitext(infile)
        abspath = os.path.join(img_dir, infile)
        ofile = os.path.join(img_dir, name + '.JPEG')
        try:
            img = Image.open(os.path.join(img_dir, abspath))
            img.convert('RGB').resize(RESOLUTION).save(ofile)
        except FileNotFoundError as e:
            print(f"The file {infile} could not be opened.")
            raise e
        except OSError as e:
            print(f"Unable to save {infile}.")
            raise e


if __name__ == '__main__':
    IMG_DIR = os.path.join(os.path.expanduser("~"), 'supplier-data', 'images')
    process_images(IMG_DIR)