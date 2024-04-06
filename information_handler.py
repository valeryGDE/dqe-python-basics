import os

from informations.custom_message import CustomMessage
from informations.news import News
from informations.private_ad import PrivateAd
import xml.etree.ElementTree as ET

from readers.json_file_reader import JsonFileReader
from readers.text_file_reader import TextFileReader
from readers.xml_file_reader import XmlFileReader


class InformationHandler:
    def __init__(self, db):
        self.db = db
        self.readers = {
            'file': TextFileReader(),
            'json': JsonFileReader(),
            'xml': XmlFileReader()
        }

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

    def _get_information_from_data(self, data):
        informations = []
        for info_data in data:
            info_type = info_data.find('InformationType').text if isinstance(info_data, ET.Element) else info_data[
                'InformationType']
            text = info_data.find('Text').text if isinstance(info_data, ET.Element) else info_data['Text']
            extra_data = info_data.find('AdditionalData').text if isinstance(info_data, ET.Element) else info_data.get(
                'AdditionalData', None)
            informations.append(self._create_information(info_type, text, extra_data))
        return informations

    def process_and_delete(self, filepath, process_type):
        reader = self.readers.get(process_type)
        if not reader:
            raise ValueError(f"Unsupported process type: {process_type}")

        data = reader.read(filepath)
        informations = self._get_information_from_data(data)

        successful_process = False
        for info_object in informations:
            if info_object.append_info_to_file_and_db(self.db):
                successful_process = True

        if successful_process:
            os.remove(filepath)
            print(f"The {process_type} '{filepath}' has been successfully processed and deleted.")
        else:
            print(f"The {process_type} was not processed successfully, so it will not be deleted.")

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
