from datetime import datetime
from informations.information import Information


class News(Information):
    def __init__(self, text, city, date=datetime.now()):
        super().__init__(text, f'{city}, {date.strftime("%d/%m/%Y %H.%M")}')

    def append_info_to_db(self, db):
        if db.record_exists("News", Text=self.text):
            print(f"Duplicate information: {self.text}")
            return False
        else:
            db.insert_record("News", Text=self.text, City=self.footer.split(',')[0], Date=self.footer.split(',')[1])
            return True
