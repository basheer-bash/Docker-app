from flask import Flask, jsonify # type: ignore
import mysql.connector # type: ignore
import os

app = Flask(__name__)

# Global counter
counter = 0

# إعداد الاتصال بقاعدة البيانات
db_config = {
"host": "mysql-db",
"user": os.getenv("MYSQL_USER", "user"),
"password": os.getenv("MYSQL_PASSWORD", "password"),
"database": os.getenv("MYSQL_DATABASE", "mydb"),
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    global counter
    counter += 1
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!!'")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify({"message1": result[0]},{"counter": counter})


@app.route('/showcounter')
def show_counter():
    global counter
    counter =0
    counter += 1
    return jsonify({"counter": counter})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)