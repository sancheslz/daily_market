import sqlite3


class Connector:
    """ Singleton pattern to control the database connection"""

    _instance = None

    def __init__(self: object) -> None:
        self.sql = None
        self.cnc = None

    def connect(self: object) -> None:
        self.db_name = '../data.db'
        self.cnc = sqlite3.connect(self.db_name)
        self.sql = self.cnc.cursor()

    def execute(self: object, message: str) -> None:
        return self.sql.execute(message)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
