import sqlite3


class Database:
    """Generische Datenbankklasse, die sich ausschließlich um die Verbindung und

    Ausführung kümmert. Hier werden KEINE Queries hartcodiert und keine Variablen
    für Daten direkt verwaltet. Diese kommen ausschließlich aus den Repositories!
    """

    # ========================================================================#
    #                   DDL - Tabellen erstellen und definieren              #
    # ========================================================================#
    def __init__(self):
        """Initialisiert die Datenbank-Verbindung zur SQLite-Datei 'game.db'

        und stellt das Cursor-Objekt für Ausführungen bereit. Fängt Fehler beim
        Verbindungsaufbau ab.
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect("game.db")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Verbindung fehlgeschlagen: {e}")

    def create_table(self, query: str):
        """Führt DDL-Queries (Data Definition Language) aus, um neue Strukturen

        (Tabellen) in der Datenbank anzulegen. Sichert die Änderung mittels
        Commit.

        Args:
            query (str): Das vollständige SQL 'CREATE TABLE'-Statement aus dem
              Repository.
        """
        if self.conn:
            try:
                self.cursor.execute(query)
                self.conn.commit()
                print("Tabelle angelegt")
            except sqlite3.DatabaseError as e:
                print(f"Tabelle konnte nicht erstellt werden; {e}")

    def update_table(self, query: str):
        """Führt eine übergebene Query zur Manipulation oder Änderung von Daten

        aus und schreibt die Änderungen dauerhaft fest (Commit). Kann für INSERT
        oder UPDATE verwendet werden.

        Args:
            query (str): Das SQL-Statement aus dem Repository.
        """
        if self.conn:
            try:
                self.cursor.execute(query)
                self.conn.commit()
                print("Datensatz aktualisiert!")
            except sqlite3.DatabaseError as e:
                print(f"Die Tabelle konnte nicht aktualisiert werden: {e}")

    def delete_table(self, query: str):
        """Führt DDL-Befehle zum Entfernen von Datenbankstrukturen (DROP TABLE)

        aus und bestätigt die permanente Löschung auf der Festplatte.

        Args:
            query (str): Das SQL 'DROP TABLE'-Statement aus dem Repository.
        """
        if self.conn:
            try:
                self.cursor.execute(query)
                self.conn.commit()
            except sqlite3.DatabaseError as e:
                print(f"Tabelle konnte nicht gelöscht werden: {e}")

    def close_connection(self):
        """Schließt die bestehende Datenbankverbindung und gibt alle blockierten

        Systemressourcen der SQLite-Datei ordnungsgemäß frei.
        """
        if self.conn:
            try:
                self.conn.close()
                print("Datenbankverbindung erfolgreich getrennt.")
            except sqlite3.DatabaseError as e:
                print(f"Verbindung konnte nicht geschlossen werden: {e}")

    # ========================================================================#
    #                   DML - Tabelleninhalte erstellen                      #
    # ========================================================================#

    def create_dataset(self, query: str, params: dict | tuple = ()):
        """Führt eine schreibende DML-Query (INSERT) aus. Verknüpft die übergebene

        Query absolut sicher mit den Daten-Parametern (z.B. ein Dictionary mit
        benannten Platzhaltern) und schreibt die Änderungen via Commit fest.

        Args:
            query (str): Das SQL 'INSERT INTO'-Statement aus dem Repository.
            params (dict | tuple, optional): Die echten Datenwerte (z.B.
              dataset['content']). Standardwert ist ein leeres Tupel ().
        """
        if self.conn:
            try:
                self.cursor.execute(query, params)
                print("Daten erfolgreich in die Tabelle eingetragen")
                self.conn.commit()
            except sqlite3.DatabaseError as e:
                print(
                    f"Die Daten konnten nicht in die Tabelle eingetragen werden: {e}"
                )

    def read_dataset(self, query: str, params: dict | tuple = ()):
        """Führt eine lesende DML-Query (SELECT) aus. Nutzt optionale Filter-

        Parameter (z.B. für WHERE-Klauseln) und gibt alle gefundenen Datensätze
        an das aufrufende Repository zurück.

        Args:
            query (str): Das SQL 'SELECT'-Statement aus dem Repository.
            params (dict | tuple, optional): Optionale Filterwerte für die Query
              (z.B. Name/ID). Standardwert ist ein leeres Tupel ().

        Returns:
            list: Eine Liste von Tupeln, die die gefundenen Zeilen der DB
              repräsentiert.
        """
        if self.conn:
            try:
                self.cursor.execute(query, params)
                print("Daten erfolgreich ausgelesen")
                return self.cursor.fetchall()
            except sqlite3.DatabaseError as e:
                print(f"Die Daten konnten nicht gelesen werden: {e}")

    def update_dataset(self, query: str, params: dict | tuple = ()):
        """Führt eine modifizierende DML-Query (UPDATE) aus. Ändert bestehende

        Einträge anhand der übergebenen Query und Parameter ab und speichert
        sie via Commit.

        Args:
            query (str): Das SQL 'UPDATE'-Statement aus dem Repository.
            params (dict | tuple, optional): Die neuen Werte sowie
              Filterkriterien. Standardwert ist ein leeres Tupel ().
        """
        if self.conn:
            try:
                self.cursor.execute(query, params)
                print("Daten erfolgreich aktualisiert")
                self.conn.commit()
            except sqlite3.DatabaseError as e:
                print(f"Die Daten konnten nicht aktualisiert werden: {e}")

    def delete_dataset(self, query: str, params: dict | tuple = ()):
        """Führt eine löschende DML-Query (DELETE) aus. Entfernt gezielt Daten-

        Sätze basierend auf den übergebenen Parametern aus der Tabelle und
        speichert die Änderung via Commit.

        Args:
            query (str): Das SQL 'DELETE FROM'-Statement aus dem Repository.
            params (dict | tuple, optional): Die Identifikationsmerkmale (z.B.
              ID). Standardwert ist ein leeres Tupel ().
        """
        if self.conn:
            try:
                self.cursor.execute(query, params)
                print("Daten erfolgreich gelöscht")
                self.conn.commit()
            except sqlite3.DatabaseError as e:
                print(f"Die Daten konnten nicht gelöscht werden: {e}")
