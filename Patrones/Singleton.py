class Singleton:
    _intance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._intance:
            cls._intance[cls] = super().__new__(cls)
        return cls._intance[cls]

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)

import sqlite3

class DatabaseConnection(Singleton):
    connection = None

    def __init__(self):
        if self.connection is None:
            self.connection = sqlite3.connect("users.db")

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Alice')")

print(db1 is db2)