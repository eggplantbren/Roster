import apsw
from config import config

# Create/load database and keep a global instance of the cursor
# called db.
conn = apsw.Connection(config["database"])
db = conn.cursor()


def create_tables():
    """
    Create the tables
    """
    global db

    # Create the table of people
    db.execute("""
    CREATE TABLE IF NOT EXISTS people
        (id     INTEGER PRIMARY KEY,
         name   TEXT NOT NULL);
    """)

    # Create a table of tasks
    db.execute("""
    CREATE TABLE IF NOT EXISTS tasks
        (id             INTEGER PRIMARY KEY,
         name           TEXT NOT NULL,
         description    TEXT,
         interval_days  INTEGER);
    """)




def close_connection():
    """
    Close the global connection
    """
    global conn
    conn.close()

