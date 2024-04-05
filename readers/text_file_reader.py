from readers.file_reader import FileReader


class TextFileReader(FileReader):
    def read(self, filepath):
        with open(filepath, 'r') as file:
            contents = file.read().split('\n\n')
            return contents