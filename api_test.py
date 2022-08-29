import unittest
from src.api import Api
import os


class TestApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.environ_name = "testing"
        os.environ[cls.environ_name] = "test environment variable"
        cls.api_name = "TestApi"
        cls.api = Api(cls.api_name, cls.environ_name)
        cls.test_data = "test data"
        cls.full_path = f"{cls.api_name.upper()}/{cls.api_name.lower()}"
        print(cls.full_path)

    def test_save_to_file(self):
        self.api.save_to_file(self.test_data)
        # ensure directory is created
        expected_result = True
        result = os.path.isdir(self.api_name.upper())
        self.assertEqual(expected_result, result)

        # ensure file was created
        expected_result = True
        result = os.path.exists(self.full_path)
        self.assertEqual(expected_result, result)
