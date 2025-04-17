from constants import DB_HOST, DB_NAME, DB_USER, DB_PASS
import psycopg2  

def get_database_connection(): # * config
    try:
        postgres = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return postgres
    
    except Exception as e:
        print(e)