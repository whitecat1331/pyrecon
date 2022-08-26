import os

class Api:
    def __init__(self, path, env_var):
        self.path = path
        self.env_var = env_var
        self.key = os.getenv[self.env_var]

        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def save_to_file(self, data, file_name)
        if file_name:
            file_path = os.path.join(self.PATH, file_name)
            with click.open_file(file_path, 'w') as f:
                f.write(data)
