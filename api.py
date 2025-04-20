from flask import Flask, jsonify, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from database import get_database_connection

api = Flask(__name__)

CORS(api)

@api.route("/api/v1/todos", methods=["GET"])
def get_nodes():
    try:
        postgres = get_database_connection()
        cursor = postgres.cursor(cursor_factory=RealDictCursor) 

        cursor.execute("SELECT * FROM todos")
        response = cursor.fetchall()  

        return jsonify(response), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500 
    finally:
        cursor.close()
        postgres.close()

if __name__ == "__main__":
    api.run(debug=True, host='localhost', port=8000) 

