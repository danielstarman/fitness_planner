"""
    This module contains the controller and related logic.
"""

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


