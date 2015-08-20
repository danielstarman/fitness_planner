"""
    This module contains the controller and related logic.
"""

from PySide import QtCore, QtGui
from fitnessview import FitnessView
from fitnessmodel import FitnessModel



class FitnessController(object):
    """
        This class will initialize and hook up the model and the view.
    """

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.ui.add_day_button.clicked.connect(model.add_day)
        self.model.day_added.connect(self.day_added)

    @QtCore.Slot(str)
    def day_added(self, string):
        print string
