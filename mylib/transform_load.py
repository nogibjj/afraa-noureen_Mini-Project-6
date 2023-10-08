"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/baskin_icecream.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    baskin_data = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(baskin_data)
    conn = sqlite3.connect("baskin_icecream.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS baskin_icecream")
    c.execute(
        """
        CREATE TABLE baskin_icecream (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Flavour TEXT,
            Calories INTEGER,
            Total_Fat_g REAL,
            Trans_Fat_g REAL,
            Carbohydrates_g INTEGER,
            Sugars_g INTEGER,
            Protein_g REAL,
            Size TEXT
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO baskin_icecream (
            Flavour, 
            Calories, 
            Total_Fat_g, 
            Trans_Fat_g, 
            Carbohydrates_g, 
            Sugars_g, 
            Protein_g, 
            Size
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        baskin_data,
    )
    conn.commit()
    conn.close()
    return "baskin_icecream.db"
