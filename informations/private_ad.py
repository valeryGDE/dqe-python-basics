from informations.information import Information
from datetime import datetime


class PrivateAd(Information):
    def __init__(self, text, expiration_date):
        super().__init__(text, expiration_date)
        days_left = (datetime.strptime(expiration_date, '%d/%m/%Y') - datetime.now()).days
        self.footer = f'Actual until: {expiration_date}, {days_left} days left'

    def append_info_to_db(self, db):
        if db.record_exists("PrivateAd", Text=self.text):
            print(f"Duplicate information: {self.text}")
            return False
        else:
            db.insert_record("PrivateAd", Text=self.text, ExpirationDate=self.footer)
            return True
