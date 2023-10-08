"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def run_query(query):
    """runs the query input by the user"""
    # Connect to the SQLite database
    conn = sqlite3.connect("baskin_icecream.db")
    cursor = conn.cursor()
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    cursor.close()
    conn.close()
    log(f"{query}")


def create(
    Flavour,
    Calories,
    Total_Fat_g,
    Trans_Fat_g,
    Carbohydrates_g,
    Sugars_g,
    Protein_g,
    Size,
):
    """sample query"""
    conn = sqlite3.connect("baskin_icecream.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO baskin_icecream 
        (Flavour,Calories,Total_Fat_g,Trans_Fat_g,Carbohydrates_g,Sugars_g,Protein_g,Size) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            Flavour,
            Calories,
            Total_Fat_g,
            Trans_Fat_g,
            Carbohydrates_g,
            Sugars_g,
            Protein_g,
            Size,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log(
        f"""INSERT INTO baskin_icecream VALUES (
            {Flavour}, 
            {Calories}, 
            {Total_Fat_g}, 
            {Trans_Fat_g}, 
            {Carbohydrates_g}, 
            {Sugars_g}, 
            {Protein_g}, 
            {Size});"""
    )


def update(
    record_id,
    Flavour,
    Calories,
    Total_Fat_g,
    Trans_Fat_g,
    Carbohydrates_g,
    Sugars_g,
    Protein_g,
    Size,
):
    """sample query"""
    conn = sqlite3.connect("baskin_icecream.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE baskin_icecream 
        SET Flavour =?,
        Calories=?,
        Total_Fat_g=?,
        Trans_Fat_g=?,
        Carbohydrates_g=?,
        Sugars_g=?,
        Protein_g=?,
        Size=?
        WHERE id=?
        """,
        (
            Flavour,
            Calories,
            Total_Fat_g,
            Trans_Fat_g,
            Carbohydrates_g,
            Sugars_g,
            Protein_g,
            Size,
            record_id,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log(
        f"""UPDATE baskin_icecream SET
        Flavour={Flavour},
        Calories={Calories},
        Total_Fat_g={Total_Fat_g},
        Trans_Fat_g={Trans_Fat_g},
        Carbohydrates_g={Carbohydrates_g},
        Sugars_g={Sugars_g},
        Protein_g={Protein_g},
        Size={Size}
        WHERE id={record_id};"""
    )


def delete(record_id):
    """sample query"""
    conn = sqlite3.connect("baskin_icecream.db")
    c = conn.cursor()
    c.execute("DELETE FROM baskin_icecream WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log(f"DELETE FROM baskin_icecream WHERE id={record_id};")


def read():
    """read data"""
    conn = sqlite3.connect("baskin_icecream.db")
    c = conn.cursor()
    c.execute("SELECT * FROM baskin_icecream")
    data = c.fetchall()
    log("SELECT * FROM baskin_icecream;")
    return data
