"""
A Python script to create the 'alx_book_store' database in a MySQL server using PyMySQL.
"""

import pymysql
from pymysql.err import OperationalError

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Khutsilutsi@07"
DATABASE_NAME = "alx_book_store"

def create_database():
    """
    Connects to the MySQL server and creates the specified database.
    """
    connection = None
    try:
        # Establish a connection to the MySQL server
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            charset="utf8mb4"
        )

        with connection.cursor() as cursor:
            query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
            cursor.execute(query)
            print(f"Database '{DATABASE_NAME}' created successfully!")

    except OperationalError as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if connection:
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
