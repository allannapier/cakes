import unittest
import unittest.mock
from main import add_items
from lib import add_cake_to_s3
from lib import delete_cake_from_s3


class TestApiFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def testAddItems(self):
        exp_result = {"status":"Success"}
        data = {"name": "string","comment": "string","image_url": "string","yum_factor": 1}
        result = add_items(data)
        self.assertEqual(exp_result, result)