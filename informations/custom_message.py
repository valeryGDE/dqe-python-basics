from informations.information import Information
import random


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

    def append_info_to_db(self, db):
        if db.record_exists("CustomMessage", Text=self.text):
            print(f"Duplicate information: {self.text}")
            return False
        else:
            db.insert_record("CustomMessage", Text=self.text, Likes=self.likes)
            return True
