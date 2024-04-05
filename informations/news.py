from datetime import datetime
from informations.information import Information


class News(Information):
    def __init__(self, text, city, date=datetime.now()):
        super().__init__(text, f'{city}, {date.strftime("%d/%m/%Y %H.%M")}')
