import os
import click


class Api:
    def __init__(self, api_name, env_name):
        self.api_name = api_name.lower()
        self.dir_path = api_name.upper()
        self.env_name = env_name
        self.key = os.environ.get(self.env_name)
        self.full_path = os.path.join(self.dir_path, self.api_name)

    def save_to_file(self, data):
        if not os.path.isdir(self.dir_path):
            os.mkdir(self.dir_path)

        with click.open_file(self.full_path, "w") as f:
            f.write(data)
