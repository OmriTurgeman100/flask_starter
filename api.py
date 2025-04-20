from flask import Flask, jsonify, request
from flask_cors import CORS
from psycopg2.extras import RealDictCursor
from database import get_database_connection
from threading import Thread


api = Flask(__name__)

CORS(api)

@api.route("/api/v1/todos", methods=["GET"])
def get_todos():
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


@api.route("/api/v1/todos/<id>", methods=["GET"])
def get_specific_todo(id):
    try:
        postgres = get_database_connection()
        cursor = postgres.cursor(cursor_factory=RealDictCursor) 

        print(id)

        cursor.execute("select * from todos where id = %s", (id,))
        response = cursor.fetchall()  

        return jsonify(response), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500 
    finally:
        cursor.close()
        postgres.close()


@api.route("/api/v1/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    try:
        postgres = get_database_connection()
        cursor = postgres.cursor(cursor_factory=RealDictCursor) 

        cursor.execute("delete from todos where id = %s", (id))

        postgres.commit()

        # response = cursor.fetchall()  

        return jsonify("todo deleted 200"), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500 
    finally:
        cursor.close()
        postgres.close()



@api.route("/api/v1/todos/post", methods=["POST"])
def post_todo():
    try:
        postgres = get_database_connection()
        cursor = postgres.cursor(cursor_factory=RealDictCursor) 

        data = request.json

        title = data.get('title')
        description = data.get('description')

        # print(title, description)

        cursor.execute("insert into todos (title, description) values (%s, %s) returning *", (title, description))

        postgres.commit()

        response = cursor.fetchall()  

        heavy_work(title)

        # thread = Thread(target=(heavy_work), args=(title,))
        # thread.start()

        return jsonify(response), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500 
    finally:
        cursor.close()
        postgres.close()


def heavy_work(title):
    try:

        print(f"specified title is ${title}")

        number = 0

        while True:
            number += 1
            print(number)

    except Exception as e:
        print(e)


@api.route("/api/v1/todos/patch/<id>", methods=["PATCH"])
def patch_todo(id):
    try:
        postgres = get_database_connection()
        cursor = postgres.cursor(cursor_factory=RealDictCursor) 

        data = request.json

        title = data.get('title')
        # description = data.get('description')

        # print(title, description)

        cursor.execute("update todos set title = %s where id = %s returning *", (title, id))

        postgres.commit()

        response = cursor.fetchall()  

        return jsonify(response), 200
        
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500 
    finally:
        cursor.close()
        postgres.close()

if __name__ == "__main__":
   api.run(debug=False, host='localhost', port=8000, threaded=False)


