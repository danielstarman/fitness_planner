"""
    This module contains the controller and related logic.
"""

from PySide import QtCore, QtGui
from fitnessview import FitnessView
from fitnessmodel import FitnessModel



class FitnessController(QtCore.QObject):
    """
        This class will initialize and hook up the model and the view.
    """
    day_label_created = QtCore.Signal(str)

    def __init__(self, model, view):
        super(FitnessController, self).__init__()
        self.model = model
        self.view = view

        self.view.ui.add_day_button.clicked.connect(model.add_day)
        self.model.day_added.connect(self.day_added)
        self.day_label_created.connect(self.view.add_day_label)

    @QtCore.Slot(str)
    def day_added(self, string):
        self.day_label_created.emit(string)



