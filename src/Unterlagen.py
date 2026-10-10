from data.database import Database

class Unterlagen:

    def __init__(self):
        self.db = Database()

        if self.db.conn:
            print("Datenbankverbindung erfolgreich aufgebaut")

    def new_file(self):
        dataset = {
                "tablename": "unterlagen",
                "content": {
                    "dateiformat": "pdf",
                    "titel": "Python für Anfänger - Band 3",
                    "inhalt": "Lorem ipsum dolor sit amet..."
                }
            }
        table = dataset["tablename"]
        params = dataset["content"]
        spalten = ", ".join(params.keys())

        platzhalter = ", ".join([f":{k}" for k in params.keys()])
        query = f"INSERT INTO {table} ({spalten}) VALUES({platzhalter})"
        self.db.create_dataset(query, params)
        
    def show_single_file(self):
         print(self.db.read_dataset("SELECT * FROM unterlagen"))