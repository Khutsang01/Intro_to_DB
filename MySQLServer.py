"""
A Python script to create the 'alx_book_store' database in a MySQL server.
"""

import mysql.connector
from mysql.connector import Error

# Replace with your actual MySQL credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Khutsilutsi@07"
DATABASE_NAME = "alx_book_store"

def create_database():
    """
    Connects to the MySQL server and creates the specified database.
    
    The script uses CREATE DATABASE IF NOT EXISTS to avoid errors if the
    database already exists.
    """
    connection = None
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            auth_plugin="mysql_native_password"   # 👈 Force correct plugin
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Use CREATE DATABASE IF NOT EXISTS to handle existence gracefully
            query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
            cursor.execute(query)

            print(f"Database '{DATABASE_NAME}' created successfully!")

    except Error as e:
        # Handle connection and other potential errors
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Ensure the connection is closed
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
