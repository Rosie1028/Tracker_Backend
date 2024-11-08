import psycopg2
from flask import jsonify, current_app, g

def get_db():
    if 'db' not in g:
        try:
            g.db = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="postgres",
                host="localhost",
            )
        except psycopg2.Error as e:
            current_app.logger.error(f"Database connection error: {e}")
            g.db = None

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        try:
            db.close()
        except psycopg2.Error as e:
            current_app.logger.error(f"Database close error: {e}")

def execute_query(query, params=None):
    db = get_db()
    if db is None:
        return None

    try:
        with db.cursor() as cursor:
            cursor.execute(query, params)
            db.commit()
            return cursor.fetchall()
    except psycopg2.Error as e:
        current_app.logger.error(f"Query execution error: {e}")
        return None