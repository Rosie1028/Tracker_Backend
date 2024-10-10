from flask import request, jsonify
from data.models import Workout
from data_access.data_access import insert_workout, get_all_workouts, get_workout_by_day, get_workout_by_date, \
    get_workout_by_type, update_workout, get_workout_by_id
from . import api_blueprint

@api_blueprint.route('/workouts', methods=['GET'])
def get_workouts():
    """
    Retrieves all workout records.

    Returns:
        Response: A JSON response containing all workout records.
    """
    return get_all_workouts()

@api_blueprint.route('/workouts', methods=['POST'])
def create_workout():
    """
    Creates a new workout record.

    Returns:
        Response: A JSON response containing the created workout record and a status code 201 on success.
        Response: A JSON response containing an error message and a status code 400 on failure.
    """
    try:
        day = request.args.get('day')
        date = request.args.get('date')
        tipe = request.args.get('type')
        reps = request.args.get('reps', 0)
        weight = request.args.get('weight', 0)
        duration = int(request.args.get('duration', 0))

        workout = Workout(day, date, tipe, reps, weight, duration)
        insert_workout(workout)
        return jsonify(workout.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api_blueprint.route('/workouts/day/<day>', methods=['GET'])
def get_workouts_by_day(day):
    """
    Retrieves all workout records for a specific day.

    Args:
        day (str): The day to filter workouts by.

    Returns:
        Response: A JSON response containing all workout records for the specified day.
    """
    try:
        workouts = get_workout_by_day(day)
        return jsonify([workout for workout in workouts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api_blueprint.route('/workouts/date/<date>', methods=['GET'])
def get_workouts_by_date(date):
    """
    Retrieves all workout records for a specific date.

    Args:
        date (str): The date to filter workouts by.

    Returns:
        Response: A JSON response containing all workout records for the specified date.
    """
    try:
        workouts = get_workout_by_date(date)
        return jsonify([workout for workout in workouts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



@api_blueprint.route('/workouts/type/<workout_type>', methods=['GET'])
def get_workouts_by_type(workout_type):
    """
    Retrieves all workout records for a specific type.

    Args:
        workout_type (str): The type to filter workouts by.

    Returns:
        Response: A JSON response containing all workout records for the specified type.
    """
    try:
        workouts = get_workout_by_type(workout_type)
        return jsonify([workout for workout in workouts]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@api_blueprint.route('/workouts/<int:idd>', methods=['PUT'])
def update_workout(idd):
    """
    Updates an existing workout record.

    Args:
        idd (int): The ID of the workout to update.

    Returns:
        Response: A JSON response containing the updated workout record and a status code 200 on success.
        Response: A JSON response containing an error message and a status code 400 on failure.
    """
    try:
        workout = get_workout_by_id(idd)
        if not workout:
            return jsonify({'error': 'Workout not found'}), 404

        workout.day = request.args.get('day', workout['day'])
        workout.date = request.args.get('date', workout['date'])
        workout.tipe = request.args.get('type', workout['type'])
        workout.reps = request.args.get('reps', workout['reps'])
        workout.weight = request.args.get('weight', workout['weight'])
        workout.duration = int(request.args.get('duration', workout['duration']))

        update_workout(idd,workout)
        return jsonify(workout), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400








