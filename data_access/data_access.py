import psycopg2
from flask import jsonify

from data.models import Workout

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres")
    return conn

connection = get_db_connection()
cur = connection.cursor()

def insert_workout(workout):
    try:
        print(type(workout.id))

        sql = ''' INSERT INTO workouts(id, day, date, reps, weight, duration)
                  VALUES (%s, %s, %s, %s, %s, %s) '''
        cur.execute(sql, (workout.id, workout.day, workout.date, workout.reps, workout.weight, workout.duration))
        connection.commit()
        print(f"Workout added with id: {workout.id}")
        return cur.lastrowid
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()

def get_all_workouts():
    try:
        cur.execute('SELECT * FROM workouts;')
        data = cur.fetchall()
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()
