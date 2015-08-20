"""
    The main module.
"""
import sys
from PySide import QtGui, QtCore
from fitnessmodel import FitnessModel
from fitnesscontroller import FitnessController
from fitnessview import FitnessView

class App(QtGui.QApplication):

    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = FitnessModel()
        self.view = FitnessView()
        self.controller = FitnessController(self.model, self.view)
        self.view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())