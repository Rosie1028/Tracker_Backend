from flask import Flask, jsonify
import psycopg2
from api.routes import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')


def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn


@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM workouts;')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5001)