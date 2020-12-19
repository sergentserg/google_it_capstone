#!/usr/bin/env python3
import unittest
import os
import PIL

from change_image import RESOLUTION, process_images


class TestProcessImages(unittest.TestCase):
    def setUp(self):
        self.test_dir = test_dir = os.path.join(os.environ.get("TEMP"), 'test_images')
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)
        os.mkdir(self.test_dir)

        # Save a test image.
        self.test_fp = os.path.join(self.test_dir, 'test_image')
        test_dimensions = (1000, 1000)
        PIL.Image.new('RGBA', test_dimensions).save(os.path.join(self.test_fp + '.png'))

    def test_process_images(self):
        expected = (RESOLUTION, 'JPEG')
        process_images(self.test_dir)
        test_image = PIL.Image.open(self.test_fp + '.jpeg')
        self.assertEqual(expected, (test_image.size, test_image.format))
