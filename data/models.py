# Define your data models here
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {'id': self.id, 'name': self.name}


class Workout:
    def __init__(self, id, day, reps, weight, duration):
        self.id = id
        self.day = day
        self.reps = reps
        self.weight = weight
        self.duration = duration

    def __repr__(self):
        return f"Workout(id={self.id}, day='{self.day}', reps={self.reps}, weight={self.weight}, duration={self.duration})"


