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


def get_workout_by_day(day):
    """
    Retrieves all workout records for a specific day from the workouts table.

    Args:
        day (str): The day to filter workouts by.

    Returns:
        Response: A JSON response containing all workout records for the specified day.

    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        sql = ''' SELECT * FROM workouts WHERE day = %s; '''
        cur.execute(sql, (day,))
        data = cur.fetchall()

        # Convert the data to a list of dictionaries
        column_names = [desc[0] for desc in cur.description]
        result = [dict(zip(column_names, row)) for row in data]
        return result
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 400
    finally:
        cur.close()
        connection.close()


def get_workout_by_date(date):
    """
    Retrieves all workout records for a specific date from the workouts table.

    Args:
        date (str): The date to filter workouts by.

    Returns:
        Response: A JSON response containing all workout records for the specified date.

    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        sql = ''' SELECT * FROM workouts WHERE date = %s; '''
        cur.execute(sql, (date,))
        data = cur.fetchall()

        # Convert the data to a list of dictionaries
        column_names = [desc[0] for desc in cur.description]
        result = [dict(zip(column_names, row)) for row in data]
        print(result)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 400
    finally:
        cur.close()
        connection.close()


def get_workout_by_type(workout_type):
    """
    Retrieves all workout records for a specific type from the workouts table.

    Args:
        workout_type (str): The type to filter workouts by.

    Returns:
        Response: A JSON response containing all workout records for the specified type.

    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        sql = ''' SELECT * FROM workouts WHERE type = %s; '''
        cur.execute(sql, (workout_type,))
        data = cur.fetchall()

        # Convert the data to a list of dictionaries
        column_names = [desc[0] for desc in cur.description]
        result = [dict(zip(column_names, row)) for row in data]
        return result
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 400
    finally:
        cur.close()
        connection.close()




def update_workout(workout_id, workout):
    """
    Updates a workout record in the workouts table.

    Args:
        workout_id (int): The ID of the workout to update.
        workout (object): An object containing updated workout details such as day, date, type, reps, weight, and duration.

    Raises:
        Exception: If there is an error during the update process.
    """
    try:
        sql = ''' UPDATE workouts
                  SET day = %s, date = %s, type = %s, reps = %s, weight = %s, duration = %s
                  WHERE id = %s; '''
        cur.execute(sql, (workout.day, workout.date, workout.tipe, workout.reps, workout.weight, workout.duration, workout_id))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()



##Helper functions
def get_workout_by_id(workout_id):
    """
    Retrieves a workout record from the workouts table by its ID.

    Args:
        workout_id (int): The ID of the workout to retrieve.

    Returns:
        dict: A dictionary containing the workout details such as day, date, type, reps, weight, and duration.

    Raises:
        Exception: If there is an error during the retrieval process.
    """
    try:
        sql = ''' SELECT day, date, type, reps, weight, duration
                  FROM workouts
                  WHERE id = %s; '''
        cur.execute(sql, (workout_id,))
        workout = cur.fetchone()
        if workout:
            return {
                "day": workout[0],
                "date": workout[1],
                "type": workout[2],
                "reps": workout[3],
                "weight": workout[4],
                "duration": workout[5]
            }
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        connection.close()



