"""
    This module contains the model and related logic.
"""
from PySide import QtCore, QtGui

class FitnessModel(QtCore.QObject):
    """
        This will be the class that handles the general applications logic.
    """
    day_added = QtCore.Signal(str)
    day_changed = QtCore.Signal(str)

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
    
    @QtCore.Slot(str, str)
    def day_renamed(self, old_text, new_text):
        old_text_index = self.workout_days.index(old_text)
        self.workout_days[old_text_index] = new_text
        self.day_changed.emit(new_text)