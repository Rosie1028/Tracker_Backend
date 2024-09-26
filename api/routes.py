from flask import request, jsonify

from data_access.data_access import insert_workout, get_all_workouts
from . import api_blueprint

@api_blueprint.route('/workouts', methods=['GET'])
def get_all_workouts():
    return get_all_workouts()

@api_blueprint.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    insert_workout(data)
    return jsonify({'message': 'Workout added successfully!', 'data': data}), 201



