import unittest
from src.api import Api
import os


class TApi(Api):
    def __init__(self):
        self.environ_name = "testing"
        os.environ[self.environ_name] = "test environment variable"
        self.api_name = "TestApi"
        Api.__init__(self, self.api_name, self.environ_name)

    @Api.save
    def save_file(self):
        return "Some data"


class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.tapi = TApi()
        cls.test_file = "testing"
        cls.test_data = "{}"

    def test_save_to_file(self):
        self.tapi.save_to_file(self.test_data, self.test_save_to_file)
        # ensure directory is created
        expected_result = True
        result = os.path.isdir(self.tapi.api_name.upper())
        self.assertEqual(expected_result, result)

        # ensure file was created
        expected_result = True
        result = os.path.exists("TESTAPI/test_save_to_file.json")
        self.assertEqual(expected_result, result)

    def test_save(self):
        self.tapi.save_file()
        expected_result = True
        result = os.path.exists("TESTAPI/save_file.json")
        self.assertEqual(expected_result, result)
