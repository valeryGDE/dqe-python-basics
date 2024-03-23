import os
import textwrap
from datetime import datetime
import random


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
        header_line = self._decorate_header()
        info_string = f'\n{header_line}\n{textwrap.fill(self.text, self.max_width)}\n{textwrap.fill(self.footer, self.max_width)}\n'
        return info_string

    def print_info(self):
        print(self.construct_info())

    def append_info_to_file(self):
        filepath = 'information.txt'
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write('News feed:\n')
        with open(filepath, 'a') as f:
            f.write(self.construct_info())


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


information_input = input('Choose category from News, PrivateAd, CustomMessage: ')

if information_input == 'News':
    text_input = input('Enter some text: ')
    city_input = input('Enter city: ')
    news = News(text_input, city_input)
    news.print_info()
    news.append_info_to_file()

elif information_input == 'PrivateAd':
    text_input = input('Enter some text: ')
    expiration_date_input = input('Enter expiration date in format \'DD/MM/YYYY\': ')
    private_ad = PrivateAd(text_input, expiration_date_input)
    private_ad.print_info()
    private_ad.append_info_to_file()

elif information_input == 'CustomMessage':
    text_input = input('Enter some text: ')
    custom_message = CustomMessage(text_input)
    like_input = input('Do you like this message? (yes/no): ')
    custom_message.like_message(like_input)
    custom_message.print_info()
    custom_message.append_info_to_file()

else:
    print("Invalid category. Please choose from News, PrivateAd, CustomMessage")
    exit()
