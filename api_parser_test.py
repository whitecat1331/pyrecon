import unittest
from src.api_parser import ApiParser


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.json_dict = {
            "squadName": "Super hero squad",
            "homeTown": "Metro City",
            "formed": 2016,
            "secretBase": "Super tower",
            "active": True,
            "members": [
                {
                    "name": "Molecule Man",
                    "age": 29,
                    "secretIdentity": "Dan Jukes",
                    "powers": [
                        "Radiation resistance",
                        "Turning tiny",
                        "Radiation blast",
                    ],
                },
                {
                    "name": "Madame Uppercut",
                    "age": 39,
                    "secretIdentity": "Jane Wilson",
                    "powers": [
                        "Million tonne punch",
                        "Damage resistance",
                        "Superhuman reflexes",
                    ],
                },
                {
                    "name": "Eternal Flame",
                    "age": 1000000,
                    "secretIdentity": "Unknown",
                    "powers": [
                        "Immortality",
                        "Heat Immunity",
                        "Inferno",
                        "Teleportation",
                        "Interdimensional travel",
                    ],
                },
            ],
        }

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.raw_json = """
            {
      "squadName": "Super hero squad",
      "homeTown": "Metro City",
      "formed": 2016,
      "secretBase": "Super tower",
      "active": true,
      "members": [
        {
          "name": "Molecule Man",
          "age": 29,
          "secretIdentity": "Dan Jukes",
          "powers": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
          ]
        },
        {
          "name": "Madame Uppercut",
          "age": 39,
          "secretIdentity": "Jane Wilson",
          "powers": [
            "Million tonne punch",
            "Damage resistance",
            "Superhuman reflexes"
          ]
        },
        {
          "name": "Eternal Flame",
          "age": 1000000,
          "secretIdentity": "Unknown",
          "powers": [
            "Immortality",
            "Heat Immunity",
            "Inferno",
            "Teleportation",
            "Interdimensional travel"
          ]
        }
      ]
    }
    """
        self.parser = ApiParser(self.raw_json)

    def tearDown(self):
        pass

    def test_index_into(self):
        # test list
        expected_value = TypeError
        self.assertRaises(expected_value, self.parser.index_into, 0)

        # test dict
        self.parser.index_into("members")
        self.assertRaises(expected_value, self.parser.index_into, "key")

    def test_get_current_value(self):
        expected_value = "Metro City"
        self.parser.index_into("homeTown")
        result = self.parser.get_current_value()
        self.assertEqual(expected_value, result)

    def test_get_options(self):
        # test dictionary
        expected_list = self.json_dict["members"]
        expected_dict = self.json_dict["members"][0].keys()
        self.parser.index_into("members")
        result_list = self.parser.get_options()
        self.assertEqual(expected_list, result_list)

        # test list
        self.parser.index_into(0)
        result_dict = self.parser.get_options()
        self.assertEqual(expected_dict, result_dict)

        # corrupt data
        self.parser.current_data = ""
        self.assertRaises(TypeError, self.parser.get_options)

    def test_previous_index(self):
        # first index error
        self.assertRaises(IndexError, self.parser.previous_index)

        # test previous index
        self.parser.index_into("members")
        expected_value = self.json_dict["members"]
        current_value = self.parser.get_current_value()
        self.assertEqual(expected_value, current_value)
        self.parser.previous_index()
        expected_value = self.json_dict
        current_value = self.parser.get_current_value()
        self.assertEqual(expected_value, current_value)

    def test_execute_command(self):
        # incorrect command
        self.assertRaises(ValueError, self.parser.execute_command, "Does Not Exist")

        # run command
        self.parser.execute_command("index", "homeTown")
        expected_value = self.json_dict["homeTown"]
        current_value = self.parser.get_current_value()
        self.assertEqual(expected_value, current_value)
        
    def test_get_commands(self):
        expected_value = "Commands: index, current, options, previous, help, type"
        value = self.parser.get_commands()
        self.assertEqual(expected_value, value)

    def test_type_of(self):
        # test dict
        expected_result = dict
        result = self.parser.type_of()
        self.assertEqual(expected_result, result)

    def test_reset(self):
        expected_value = self.json_dict["members"]
        self.parser.index_into("members")
        current_value = self.parser.get_current_value()
        self.assertEqual(expected_value, current_value)

        self.parser.reset()
        expected_result = self.json_dict
        result = self.parser.get_current_value()
        self.assertEqual(expected_result, result)
