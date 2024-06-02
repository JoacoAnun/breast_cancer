import pandas as pd
from sqlalchemy import create_engine
from dotenv import dotenv_values


# Load configuration from .env file
config = dotenv_values(".env")

DB_URL = config["DB_URL"]
TABLE_NAME = config["TRAINING_TABLE_NAME"]
TRAINING_DATA = config["TRAINING_DATA"]


def connect_to_db():
    """
    Connects to the database using the provided DB_URL.

    Returns:
        connection (Connection): A connection object to the database.
            Returns None if an error occurs while connecting to the database.
    """
    try:
        engine = create_engine(DB_URL)
        return engine.connect()
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


def load_data_to_table(conn, df, table_name):
    """
    Load data from a DataFrame into a SQL table.

    Parameters:
        conn (Connection): The database connection object.
        df (DataFrame): The DataFrame containing the data to be loaded.
        table_name (str): The name of the table in the database to load the data into.

    Returns:
        None

    Raises:
        Exception: If there is an error loading the data into the table.
    """
    try:
        df.to_sql(table_name, con=conn, if_exists="replace", index=False)
        print(f"Data loaded successfully into table {table_name}")
    except Exception as e:
        print(f"Error loading data into table {table_name}: {e}")


def main():
    """
    Main function to load data from CSV into a SQL table.
    """
    conn = connect_to_db()
    if conn is not None:
        df = pd.read_csv(TRAINING_DATA)
        load_data_to_table(conn, df, TABLE_NAME)
    else:
        print("Failed to connect to the database. Exiting...")


if __name__ == "__main__":
    main()
