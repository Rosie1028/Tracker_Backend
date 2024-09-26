# # Define your data models here
# class User:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def to_dict(self):
#         return {'id': self.id, 'name': self.name}


class Workout:
    def __init__(self, id, day, date, reps, weight, duration):
        self.id = id
        self.day = day
        self.date = date
        self.reps = reps
        self.weight = weight
        self.duration = duration




