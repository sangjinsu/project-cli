import os
from rich import print


class Semantic:
    # It needs to be modified to suit the team convention.
    def __init__(self, semantic: str):
        semantics: dict[str, str] = dict(
            controller='controllers',
            co='controllers',
            service='services',
            s='services',
            repository='repositories',
            r='repositories',
            model='models',
            m='models'
        )
        self.folder_name = semantics.get(semantic)
        self.file_name = semantics.get(semantic)

    def get_folder_name(self) -> str | None:
        return self.folder_name

    def get_file_name(self) -> str | None:
        return self.file_name


def generate_file(semantic: str, package_name: str, path: str = ''):
    folder_name = Semantic(semantic).folder_name
    if folder_name is None:
        print(f'semantic {semantic} not found')
        exit(code=0)

    try:
        # Create the folder if it doesn't exist
        os.makedirs(os.path.join(path, folder_name), exist_ok=True)

        # Create the Golang file with the same name as the folder
        go_file_name = os.path.join(path, folder_name, folder_name + ".go")
        go_code = f'package {package_name}'

        with open(go_file_name, 'w') as go_file:
            go_file.write(go_code)

        print(f"Golang folder '{folder_name}' and file '{go_file_name}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")


def new_package(package_name):
    try:
        os.makedirs(package_name, exist_ok=True)
        semantics = ['co', 's', 'r', 'm']
        for semantic in semantics:
            generate_file(semantic, package_name, package_name)
    except Exception as e:
        print(f"Error: {e}")
