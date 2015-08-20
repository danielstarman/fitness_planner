"""
    This module contains the model and related logic.
"""
from PySide import QtCore, QtGui

class FitnessModel(QtCore.QObject):
    """
        This will be the class that handles the general applications logic.
    """
    day_added = QtCore.Signal(str)

    def __init__(self, workout_days=None):
        super(FitnessModel, self).__init__()
        if workout_days == None:
            workout_days = []
        self.workout_days = workout_days

    @QtCore.Slot()
    def add_day(self):
        string = 'Day {}'.format(str(len(self.workout_days) + 1))
        self.workout_days.append(string)
        self.day_added.emit(string)

