import configparser
from sqlalchemy import create_engine
import psycopg2
import pandas as pd

config = configparser.ConfigParser()
config.read('config.txt')

user = config.get('postgres', 'user')
password = config.get('postgres', 'password')
host = config.get('postgres', 'host')
port = config.get('postgres', 'port')
db = config.get('postgres', 'db')
# table_name = config.get('postgres', 'table_name')

postgres_url = f'postgresql://{user}:{password}@{host}:{port}/{db}'
engine = create_engine(postgres_url)

def get_connection():
    try:
        return psycopg2.connect(
            user = user,
            password = password,
            host = host,
            port = port,
            database = db
        )
    except:
        return False

"""using sql with params in postgres"""
# from psycopg2.extensions import AsIs



def insert_airports():
    """add airport data in postgres"""
    file_path = 'airports.csv'
    # Read the CSV with pandas
    df = pd.read_csv(file_path)

    # Clean column names (optional: make PostgreSQL-safe)
    df.columns = [col.lower() for col in df.columns]
    table_name = 'airports'

    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"✅ CSV imported successfully into table '{table_name}' in your PostgreSQL database.")



""" create new table"""

# def create_tables():
#     """ create tables in the PostgreSQL database"""
#     commands = (
#         """
#         CREATE TABLE student (
#             student_id SERIAL PRIMARY KEY,
#             student_name VARCHAR(255) NOT NULL
#         )
#         """,
#         """ CREATE TABLE grade (
#                 grade_id SERIAL PRIMARY KEY,
#                 grade_name VARCHAR(255) NOT NULL
#                 )
#         """,
#         """
#         CREATE TABLE student_grade (
#                 grade_id INTEGER PRIMARY KEY,
#                 file_extension VARCHAR(5) NOT NULL,
#                 drawing_data BYTEA NOT NULL,
#                 FOREIGN KEY (grade_id)
#                 REFERENCES grade (grade_id)
#                 ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """,
#         """
#         CREATE TABLE student_detail (
#                 student_id INTEGER NOT NULL,
#                 grade_id INTEGER NOT NULL,
#                 PRIMARY KEY (student_id , grade_id),
#                 FOREIGN KEY (student_id)
#                     REFERENCES student (student_id)
#                     ON UPDATE CASCADE ON DELETE CASCADE,
#                 FOREIGN KEY (grade_id)
#                     REFERENCES grade (grade_id)
#                     ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """)
#     conn = None
#     try:
#         # read the connection parameters
#         params = config()
#         # connect to the PostgreSQL server
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         # create table one by one
#         for command in commands:
#             cur.execute(command)
#         # close communication with the PostgreSQL database server
#         cur.close()
#         # commit the changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()

""" insert data """
# cursor.execute('''INSERT INTO Geeky(name , state)\
#     VALUES ('Babita','Bihar')''')
# cursor.execute(
#     '''INSERT INTO Geeky(name , state)\
#     VALUES ('Anushka','Hyderabad')''')
# cursor.execute(
#     '''INSERT INTO Geeky(name , state)\
#     VALUES ('Anamika','Banglore')''')
# cursor.execute('''INSERT INTO Geeky(name , state)\
#     VALUES ('Sanaya','Pune')''')
# cursor.execute(
#     '''INSERT INTO Geeky(name , state)\
#     VALUES ('Radha','Chandigarh')''')

"""update data"""
# sql1 = "UPDATE Geeky SET state = 'Haryana' WHERE name = 'Radha'"
# cursor.execute(sql1)

# # Commit your changes in the database
# conn.commit()





if __name__ == "__main__":
    openSky_api_access()