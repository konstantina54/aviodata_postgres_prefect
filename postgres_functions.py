import configparser
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import OperationalError, Error
import pandas as pd

config = configparser.ConfigParser()
config.read('config.txt')


db_config = {
    'user': config.get('postgres', 'user'),
    'password': config.get('postgres', 'password'),
    'host': config.get('postgres', 'host'),
    'port': config.get('postgres', 'port'),
    'dbname': config.get('postgres', 'db')
}
# table_name = config.get('postgres', 'table_name')


def get_engine():
    """Returns a SQLAlchemy engine."""
    conn_str = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    return create_engine(conn_str)



def insert_airports():
    """add airport data in postgres"""
    file_path = 'airports.csv'
    # Read the CSV with pandas
    df = pd.read_csv(file_path)

    # Clean column names (optional: make PostgreSQL-safe)
    df.columns = [col.lower() for col in df.columns]
    table_name = 'airports'
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"✅ CSV imported successfully into table '{table_name}' in your PostgreSQL database.")


def insert_ip_safely(ip_address, db_config):
    """
    Create `ip_addresses` table if it doesn't exist,
    then insert a single IP address.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ip_addresses (
        id SERIAL PRIMARY KEY,
        ip TEXT NOT NULL
    );
    """

    insert_sql = "INSERT INTO ip_addresses (ip) VALUES (%s);"

    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # 1. Create the table if it doesn't exist
        cursor.execute(create_table_sql)

        # 2. Insert the new row
        cursor.execute(insert_sql, (ip_address,))

        conn.commit()

        print(f"✅ IP '{ip_address}' inserted successfully.")

    except OperationalError as op_err:
        print(f"❌ Database connection failed: {op_err}")

    except Error as db_err:
        print(f"❌ Error inserting data: {db_err}")
        conn.rollback()

    finally:
        # Clean up resources
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

def add_ip_data(df):
    engine = get_engine()
    table_name = "location_data"
    df.to_sql(table_name, engine, if_exists="append", index=False)

    print(f"Data inserted into table '{table_name}'.")