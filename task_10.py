from database_handler import DatabaseHandler

db_handler = DatabaseHandler('mydatabase.db')
db_handler.create_table("""
CREATE TABLE News (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Text TEXT,
    City TEXT,
    Date TEXT
)
""")

db_handler.create_table("""
CREATE TABLE PrivateAd (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Text TEXT,
    ExpirationDate TEXT
)
""")

db_handler.create_table("""
CREATE TABLE CustomMessage (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Text TEXT,
    Likes INTEGER
)
""")
