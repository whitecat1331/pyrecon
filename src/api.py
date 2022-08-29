import os
import click


class Api:
    def __init__(self, api_name, env_name):
        self.api_name = api_name
        self.dir_path = api_name.upper()
        self.env_name = env_name
        self.key = os.environ.get(self.env_name)

    # add file_name parameter
    def save_to_file(self, data, file_name):
        if not os.path.isdir(self.dir_path):
            os.mkdir(self.dir_path)

        full_path = os.path.join(self.dir_path, file_name) + ".json"

        with click.open_file(full_path, "w") as f:
            f.write(data)
