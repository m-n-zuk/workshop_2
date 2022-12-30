from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

CREATE_DB = "CREATE DATABASE workshop;"

CREATE_USERS_TAB = """CREATE TABLE users(
    id serial PRIMARY KEY, 
    username varchar(255) UNIQUE,
    hashed_password varchar(80))"""

CREATE_MESSAGES_TAB = """CREATE TABLE messages(
    id SERIAL, 
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""


USER = "postgres"
PASSWORD = "1324"
HOST = "127.0.0.1"

try:
    cnx = connect(database="workshop", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created successfully!")
    except DuplicateDatabase as e:
        print("Database exists: ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)

try:
    cnx = connect(database="workshop", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()

    try:
        cursor.execute(CREATE_USERS_TAB)
        print("Table users created successfully!")
    except DuplicateTable as e:
        print("Table exists: ", e)

    try:
        cursor.execute(CREATE_MESSAGES_TAB)
        print("Table messages created successfully!")
    except DuplicateTable as e:
        print("Table exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)
