import requests
import json

class ApiParser:

    def __init__(self, raw_json):
        self.data = json.loads(raw_json)
        self.current_data = self.data
        self.index_chain = []
        # create exit command
        self.PARSER_COMMANDS = {
                "index": self.index_into, 
                "current": self.show_current_value, 
                "values": self.display_values, 
                "previous": self.previous_index, 
                "help": self.get_api_commands, 
                "type": self.type_of
                }

    def index_into(self, index):
        if isinstance(self.current_data, list):
            if not isinstance(index, int):
                raise TypeError("must enter a index")

        elif isinstance(self.current_data, dict):
            if not isinstance(index, str):
                raise TypeError("must enter a key")

        else:
            return TypeError("can only index into dictionaries or lists")

        self.index_chain.append(index)
        self.current_data = self.current_data[index]

    # show current data
    def show_current_value(self):
        return self.current_data

    # print the options for a list and a dictionary.
    def display_values(self):
        if isinstance(self.current_data, list):
            return self.current_data

        elif isinstance(self.current_data, dict):
            return self.current_data.keys()

        else:
            raise TypeError("can only display a dictionary or list")

    def previous_index(self):
        if not self.index_chain:
            raise IndexError("cannot index to previous while on first index")
        self.index_chain.pop()
        self.reset()
        # reset the current data
        for chain in self.index_chain:
            self.current_data = self.current_data[chain]

    def execute_command(self, command):
        self.iterating = True
        if command not in self.PARSER_COMMANDS:
            raise ValueError(f"Invaild command. \nCommands {self.get_api_commands()}")
        else:
            self.PARSER_COMMANDS[command]()

    def get_api_commands(self):
        return f"Commands: {''.join([str(command) + ', ' if command != list(self.PARSER_COMMANDS)[-1] else str(command) for command in self.PARSER_COMMANDS])}"

    def type_of(self):
        return type(self.current_data)

    def reset(self):
        self.current_data = self.data

        
