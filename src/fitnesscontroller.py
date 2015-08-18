"""
    This module contains the controller and related logic.
"""

from fitnessview import FitnessView
from fitnessmodel import FitnessModel



class FitnessController(object):
    """
        This class will initialize and hook up the model and the view.
    """

    def __init__(self):
        self.model = FitnessModel()
        self.view = FitnessView()

