import configparser
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import OperationalError, Error
import pandas as pd
from pandas import json_normalize
from datetime import datetime, UTC, timedelta
from prefect import task


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

@task (log_prints = True)
def get_engine():
    """Returns a SQLAlchemy engine."""
    conn_str = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    return create_engine(conn_str)


@task (log_prints = True)
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

    # print(f"✅ CSV imported successfully into table '{table_name}' in your PostgreSQL database.")

@task (log_prints = True)
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

        # print(f"✅ IP '{ip_address}' inserted successfully.")

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


@task (log_prints = True)
def add_ip_data(df):
    print(df)
    engine = get_engine()
    table_name = "location_data"
    df.to_sql(table_name, engine, if_exists="append", index=False)

    print(f"Data inserted into table '{table_name}'.")



@task (log_prints = True)
def get_airports_by_region(region):
    """extract posgres data about long and latitude based on users country"""
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    try:
        with conn.cursor() as cur:
            query = """
                SELECT latitude_deg, longitude_deg, icao_code
                FROM airports
                WHERE iso_country = %s
            """
            cur.execute(query, (region,))
            results = cur.fetchall()
        return results

    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return []


    return results
  

@task (log_prints = True)
def postgres_flights_data(data, flight_type):
    # data = [{'icao24': '404e72', 'firstSeen': 1754406675, 'estDepartureAirport': 'EGBG', 'lastSeen': 1754408592, 'estArrivalAirport': 'EGWN', 'callsign': 'GEDGA   ', 'estDepartureAirportHorizDistance': 1732, 'estDepartureAirportVertDistance': 443, 'estArrivalAirportHorizDistance': 1570, 'estArrivalAirportVertDistance': 9, 'departureAirportCandidatesCount': 0, 'arrivalAirportCandidatesCount': 5}, {'icao24': '40605b', 'firstSeen': 1754405523, 'estDepartureAirport': 'EGHN', 'lastSeen': 1754407967, 'estArrivalAirport': 'EGWN', 'callsign': 'GOLEW   ', 'estDepartureAirportHorizDistance': 1712, 'estDepartureAirportVertDistance': 234, 'estArrivalAirportHorizDistance': 13764, 'estArrivalAirportVertDistance': 59, 'departureAirportCandidatesCount': 1, 'arrivalAirportCandidatesCount': 4}]
    df = pd.DataFrame(data)
    yesterday_utc = datetime.now(UTC) - timedelta(days=1)
    df["flight_date"] = yesterday_utc
    engine = get_engine()
    if flight_type == 'a':
        df.to_sql(
        name="arrivals",
        con=engine,
        if_exists="append",   # 'replace' to drop/create, 'append' to add rows
        index=False
    )
    elif flight_type == 'd':
                    df.to_sql(
        name="departures",
        con=engine,
        if_exists="append",   # 'replace' to drop/create, 'append' to add rows
        index=False
    )


if __name__ == "__main__":
    postgres_arrivals()