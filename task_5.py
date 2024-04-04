import json
import os
import textwrap
from datetime import datetime
import random
from task_3 import capitalize_text
from task_7 import word_count, letter_analysis


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


class News(Information):
    def __init__(self, text, city, date=datetime.now()):
        super().__init__(text, f'{city}, {date.strftime("%d/%m/%Y %H.%M")}')


class PrivateAd(Information):
    def __init__(self, text, expiration_date):
        super().__init__(text, expiration_date)
        days_left = (datetime.strptime(expiration_date, '%d/%m/%Y') - datetime.now()).days
        self.footer = f'Actual until: {expiration_date}, {days_left} days left'


class CustomMessage(Information):
    def __init__(self, text):
        self.likes = random.randint(0, 1000)
        super().__init__(text, self.likes)

    def like_message(self, like_it):
        if like_it.lower() == 'yes':
            self.likes += 1
        elif like_it.lower() == 'no' and self.likes > 0:
            self.likes -= 1
        self.footer = f'Likes: {self.likes}'


class InformationHandler:
    def _create_information(self, info_type, text, extra_data=None):
        if info_type == 'News':
            return News(text, extra_data)
        elif info_type == 'PrivateAd':
            return PrivateAd(text, extra_data)

        elif info_type == 'CustomMessage':
            message = CustomMessage(text)
            if extra_data is not None:
                message.like_message(extra_data)
            return message
        else:
            raise ValueError("Invalid information type provided.")

    def get_information_from_file(self, filepath):
        with open(filepath, 'r') as file:
            contents = file.read().split('\n\n')
            informations = []
            for content in contents:
                lines = content.strip().split('\n')
                if len(lines) < 2:
                    continue
                info_type = lines[0].strip()
                text = lines[1].strip()
                if info_type == 'CustomMessage':
                    message = CustomMessage(text)
                    like_input = lines[2].strip() if len(lines) > 2 else None
                    message.like_message(like_input)
                    informations.append(message)
                else:
                    extra_data = lines[2].strip() if len(lines) > 2 else None
                    informations.append(self._create_information(info_type, text, extra_data))
            return informations

    def get_information_from_console(self):
        info_type = input("Enter the type of information ('News', 'PrivateAd', 'CustomMessage'): ").strip()
        text = input("Enter the text: ").strip()
        extra_data = None
        if info_type in ('News', 'PrivateAd'):
            extra_data = input(
                "Enter the city: " if info_type == 'News' else "Enter the ad expiration date (DD/MM/YYYY): ").strip()
        elif info_type == 'CustomMessage':
            like_it = input("Do you like this message? (yes/no): ").strip()
            message = self._create_information(info_type, text)
            message.like_message(like_it)
            return message
        return self._create_information(info_type, text, extra_data)

    def get_information_from_json(self, json_path):
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        informations = []
        for _, info_data in data.items():
            info_type = info_data['InformationType']
            text = info_data['Text']
            extra_data = info_data['AdditionalData'] if 'AdditionalData' in info_data else None
            informations.append(self._create_information(info_type, text, extra_data))
        return informations

    def process_and_delete(self, filepath, process_type):
        get_information = self.get_information_from_file if process_type == 'file' else self.get_information_from_json
        successful_process = False
        infos = get_information(filepath)
        for info_object in infos:
            if info_object:
                if info_object.append_info_to_file():
                    successful_process = True
        if successful_process:
            os.remove(filepath)
            print(f"The {process_type} '{filepath}' has been successfully processed and deleted.")
        else:
            print(f"The {process_type} was not processed successfully, so it will not be deleted.")


handler = InformationHandler()

input_source = input("Choose input source from a 'file', 'json', or 'console'? (file/json/console): ").strip().lower()

info = None
if input_source in ('file', 'json'):
    path = input(f"Please enter the path to the input {input_source}: ").strip()
    handler.process_and_delete(path, input_source)
elif input_source == 'console':
    info = handler.get_information_from_console()
    info.append_info_to_file()
else:
    print("Invalid input source provided. Please enter 'file', 'json', or 'console'.")
