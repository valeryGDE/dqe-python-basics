import os

from task_3 import capitalize_text
from task_7 import word_count, letter_analysis
import textwrap


class Information:
    max_width = 40

    def __init__(self, text, footer):
        self.text = text
        self.footer = footer

    def _decorate_header(self):
        header = type(self).__name__
        delimiter = '-' * (self.max_width - len(header) - 1)
        return f'{header} {delimiter}'

    def construct_info(self):
        self.text = capitalize_text(self.text)
        header_line = self._decorate_header()
        info_string = f'\n{header_line}\n{textwrap.fill(self.text, self.max_width)}\n{textwrap.fill(self.footer, self.max_width)}\n'
        return info_string

    def print_info(self):
        print(self.construct_info())

    def append_info_to_file(self):
        filepath = 'information.txt'
        try:
            if not os.path.exists(filepath):
                with open(filepath, 'w') as f:
                    f.write('News feed:\n')
            with open(filepath, 'a') as f:
                f.write(self.construct_info())
            word_count(filepath)
            letter_analysis(filepath)
            return True
        except Exception as e:
            print(f"An error occurred while appending the information to the file: {e}")
            return False

    def append_info_to_file_and_db(self, db):
        try:
            self.append_info_to_db(db)
            self.append_info_to_file()
            return True
        except Exception as e:
            print(f"An error occurred while appending the information to the file and database: {e}")
            return False

    def append_info_to_db(self, db):
        raise NotImplementedError("This method must be implemented in a subclass.")
