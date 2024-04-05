import json

from readers.file_reader import FileReader


class JsonFileReader(FileReader):
    def read(self, filepath):
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
        return data.values()
