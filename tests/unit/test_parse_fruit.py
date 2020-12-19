#!/usr/bin/env python3
import unittest
import os

from run import to_json


class TestParseFruit(unittest.TestCase):
    def setUp(self):
        self.test_fp = os.path.join(os.environ.get("TEMP"), 'test.txt')

    def test_json(self):
        name, weight, desc = "test_name", 500, "Fruit description"
        expected = {
            "name": name,
            "weight": weight,
            "description": desc,
            "image_name": os.path.basename(self.test_fp)}

        with open(self.test_fp, 'w') as f:
            f.write(f"{name}\n")
            f.write(f"{weight} lbs\n")
            f.write(f"{desc}")
        actual = to_json(self.test_fp)
        self.assertDictEqual(expected, actual)



