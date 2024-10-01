from flask import request, jsonify

from data.models import Workout
from data_access.data_access import insert_workout, get_all_workouts
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



