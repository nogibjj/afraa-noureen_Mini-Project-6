"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/baskin_icecream.csv"):
    """Transforms and Loads data into the local databricks database"""
    baskin_data = pd.read_csv(dataset, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()

        c.execute("SHOW TABLES FROM default LIKE 'baskin*'")
        result = c.fetchall()
        
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS baskin_icecream (
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
            
            for _, row in baskin_data.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO baskin_icecream VALUES {convert}")
        c.close()

    return "success"
