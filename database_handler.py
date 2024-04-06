import sqlite3


class DatabaseHandler:
    def __init__(self, db_name):
        self.db_connection = sqlite3.connect(db_name)
        self.cursor = self.db_connection.cursor()

    def create_table(self, table_query):
        self.cursor.execute(table_query)
        self.db_connection.commit()

    def insert_record(self, table_name, **values):
        columns = ', '.join(values.keys())
        placeholders = ', '.join('?' * len(values))
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", list(values.values()))
        self.db_connection.commit()

    def drop_table(self, table_name):
        self.cursor.execute(f"DROP TABLE {table_name}")
        self.db_connection.commit()

    def record_exists(self, table_name, **kwargs):
        query = f"SELECT 1 FROM {table_name} WHERE " + " AND ".join(f"{k} = ?" for k in kwargs)
        self.cursor.execute(query, tuple(kwargs.values()))
        return self.cursor.fetchone() is not None
