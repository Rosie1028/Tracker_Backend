# Define your data models here
# class User:
#     """
#     Represents a user with an ID and name.
#     """
#     def __init__(self, id, name):
#         """
#         Initializes a new User instance.
#
#         Args:
#             id (int): The user's ID.
#             name (str): The user's name.
#         """
#         self.id = id
#         self.name = name
#
#     def to_dict(self):
#         """
#         Converts the User instance to a dictionary.
#
#         Returns:
#             dict: A dictionary representation of the User instance.
#         """
#         return {'id': self.id, 'name': self.name}


class Workout:
    """
    Represents a workout with details such as day, date, type, reps, weight, and duration.
    """
    def __init__(self, day, date, tipe, reps, weight, duration):
        """
        Initializes a new Workout instance.

        Args:
            day (str): The day of the workout.
            date (str): The date of the workout.
            tipe (str): The type of workout.
            reps (int): The number of repetitions.
            weight (float): The weight used in the workout.
            duration (float): The duration of the workout in minutes.
        """
        self.day = day
        self.date = date
        self.tipe = tipe
        self.reps = reps
        self.weight = weight
        self.duration = duration

    def to_dict(self):
        """
        Converts the Workout instance to a dictionary.

        Returns:
            dict: A dictionary representation of the Workout instance.
        """
        return {
            'day': self.day,
            'date': self.date,
            'type': self.tipe,
            'reps': self.reps,
            'weight': self.weight,
            'duration': self.duration
        }