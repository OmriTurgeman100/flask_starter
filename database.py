import os
import psycopg2

def get_database_connection():
    try:
        postgres = psycopg2.connect(
            host=os.environ["DB_HOST"],
            database=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"]
        )
        return postgres

    except Exception as e:
        print(f"Database connection error: {e}")
