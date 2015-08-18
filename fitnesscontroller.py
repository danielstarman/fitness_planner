from fitnessview import FitnessView
from fitnessmodel import FitnessModel



class FitnessController(object):

    def __init__(self):
        self.model = FitnessModel()
        self.view  = FitnessView()

