import psycopg2
from flask import jsonify


def get_db_connection():
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
        conn (psycopg2.extensions.connection): A connection object to the PostgreSQL database.
    """
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres")
    return conn


connection = get_db_connection()
cur = connection.cursor()


def insert_workout(workout):
    """
    Inserts a workout record into the workouts table.

    Args:
        workout (object): An object containing workout details such as day, date, type, reps, weight, and duration.

    Raises:
        Exception: If there is an error during the insertion process.
    """
    try:
        sql = ''' INSERT INTO workouts( day, date, type, reps, weight, duration)
                  VALUES ( %s, %s, %s, %s, %s, %s) '''
        cur.execute(sql, (workout.day, workout.date, workout.tipe, workout.reps, workout.weight, workout.duration))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()


def get_all_workouts():
    """
    Retrieves all workout records from the workouts table.

    Returns:
        Response: A JSON response containing all workout records.

    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        cur.execute('SELECT * FROM workouts;')
        data = cur.fetchall()
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()
