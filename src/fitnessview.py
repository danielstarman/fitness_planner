"""
    This module contains the view and related logic..
"""
from PySide import QtCore, QtGui
from main_window import Ui_Form

class FitnessView(QtGui.QMainWindow):
    """
        This will be the class that displays and updates the UI.
    """
    def __init__(self):
        super(FitnessView, self).__init__()
        self.build_ui()
        
    def build_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        

    