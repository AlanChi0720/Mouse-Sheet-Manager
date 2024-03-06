import sqlite3
import pandas as pd

class MouseDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('mouse.db')
        self.c = self.conn.cursor()
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS mouse_data 
            (id INTEGER PRIMARY KEY, 
            cage_number INTEGER,
            mouse_number INTEGER,
            DoB TEXT)
            ''')
        self.conn.commit()

    def add_mouse(self, cage_number, mouse_number, dob):
        self.c.execute("INSERT INTO mouse_data (cage_number, mouse_number, dob) VALUES (?, ?, ?)", 
                       (cage_number, mouse_number, dob)) 
        self.conn.commit()

    def import_pandas(self):
        df = pd.read_sql_query("SELECT * FROM mouse_data", self.conn)  
        print(df)

    def delete_data(self, cage_number=None, mouse_number=None):
        if cage_number:
            self.c.execute("DELETE FROM mouse_data WHERE cage_number = ?", (cage_number,))
        elif mouse_number:
            self.c.execute("DELETE FROM mouse_data WHERE mouse_number = ?", (mouse_number,))
        else:
            self.c.execute("DELETE FROM mouse_data")
        self.conn.commit()

    def __del__(self):
        self.conn.close()