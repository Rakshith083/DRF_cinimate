import psycopg2
from decouple import config

USER=config('USER')
PASSWORD=config('PASSWORD')
HOST=config('HOST')
PORT=config('PORT')
DATABASE=config('DATABASE')
# connection establishment
class DBSetup:
    def setup():
        conn = psycopg2.connect(
        database="postgres",
            user=USER,
            password=PASSWORD,
            host=HOST,
            port= PORT
        )

        conn.autocommit = True
        
        # Creating a cursor object
        cursor = conn.cursor()
        
        # query to create a database 
        sql = 'CREATE database '+DATABASE
        
        # executing above query
        try:
            cursor.execute(sql)
            print("Database has been created successfully !!")
        except psycopg2.errors.DuplicateDatabase as e:
            print(e)
        
        # Closing the connection
        conn.close()