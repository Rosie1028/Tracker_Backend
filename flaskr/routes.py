from flask import Blueprint, request, jsonify
from flaskr.db import get_db

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    """
    Fetch all workouts from the database.

    Returns:
        JSON response containing all workouts or an error message.
    """
    try:
        db = get_db()
        query = 'SELECT * FROM workouts;'
        with db.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/workouts/day/<day>', methods=['GET'])
def get_workouts_by_day(day):
    """
    Fetch workouts by day from the database.

    Args:
        day (str): The day to filter workouts by.

    Returns:
        JSON response containing workouts for the specified day or an error message.
    """
    try:
        db = get_db()
        query = 'SELECT * FROM workouts WHERE day = %s;'
        with db.cursor() as cursor:
            cursor.execute(query, (day,))
            results = cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/workouts/date/<date>', methods=['GET'])
def get_workouts_by_date(date):
    """
    Fetch workouts by date from the database.

    Args:
        date (str): The date to filter workouts by.

    Returns:
        JSON response containing workouts for the specified date or an error message.
    """
    try:
        db = get_db()
        query = 'SELECT * FROM workouts WHERE date = %s;'
        with db.cursor() as cursor:
            cursor.execute(query, (date,))
            results = cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/workouts/type/<workout_type>', methods=['GET'])
def get_workouts_by_type(workout_type):
    """
    Fetch workouts by type from the database.

    Args:
        workout_type (str): The type of workout to filter by.

    Returns:
        JSON response containing workouts for the specified type or an error message.
    """
    try:
        db = get_db()
        query = 'SELECT * FROM workouts WHERE type = %s;'
        with db.cursor() as cursor:
            cursor.execute(query, (workout_type,))
            results = cursor.fetchall()
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/workouts', methods=['POST'])
def create_workout():
    """
    Create a new workout entry in the database.

    Returns:
        JSON response containing the created workout or an error message.
    """
    try:
        workout = {
            'day': request.args.get('day'),
            'date': request.args.get('date'),
            'type': request.args.get('type'),
            'reps': request.args.get('reps'),
            'weight': request.args.get('weight'),
            'duration': int(request.args.get('duration'))
        }

        db = get_db()
        query = '''INSERT INTO workouts(day, date, type, reps, weight, duration)
                   VALUES (%s, %s, %s, %s, %s, %s)'''

        with db.cursor() as cursor:
            cursor.execute(query, (
                workout['day'], workout['date'], workout['type'], workout['reps'], workout['weight'], workout['duration']))
            db.commit()

        return jsonify(workout), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    """
    Update an existing workout entry in the database.

    Args:
        id (int): The ID of the workout to update.

    Returns:
        JSON response containing the updated workout or an error message.
    """
    try:
        workout = {
            'day': request.args.get('day'),
            'date': request.args.get('date'),
            'type': request.args.get('type'),
            'reps': request.args.get('reps'),
            'weight': request.args.get('weight'),
            'duration': int(request.args.get('duration'))
        }

        db = get_db()
        query = '''UPDATE workouts
                   SET day = %s, date = %s, type = %s, reps = %s, weight = %s, duration = %s
                   WHERE id = %s'''

        with db.cursor() as cursor:
            cursor.execute(query, (
                workout['day'], workout['date'], workout['type'], workout['reps'], workout['weight'], workout['duration'], id))
            db.commit()

        return jsonify(workout), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500










