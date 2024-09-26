from . import api_blueprint
@api_blueprint.route('/hello', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

@api_blueprint.route('/myworkouts', methods=['GET', 'POST', 'PUT', 'DELETE'])
def show_workouts():
    return {'message': "Here you can see and update workouts"}
