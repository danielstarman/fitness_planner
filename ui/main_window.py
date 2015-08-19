# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Aug 19 12:55:10 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 571)
        self.tutorial_video = phonon.Phonon.VideoPlayer(Form)
        self.tutorial_video.setGeometry(QtCore.QRect(250, 0, 300, 200))
        self.tutorial_video.setObjectName("tutorial_video")
        self.tutorial_button = QtGui.QPushButton(Form)
        self.tutorial_button.setGeometry(QtCore.QRect(360, 210, 75, 23))
        self.tutorial_button.setObjectName("tutorial_button")
        self.workout_day_combo = QtGui.QComboBox(Form)
        self.workout_day_combo.setGeometry(QtCore.QRect(630, 10, 141, 22))
        self.workout_day_combo.setObjectName("workout_day_combo")
        self.add_day_button = QtGui.QPushButton(Form)
        self.add_day_button.setGeometry(QtCore.QRect(780, 10, 75, 23))
        self.add_day_button.setObjectName("add_day_button")
        self.muscle_group_table = QtGui.QTableWidget(Form)
        self.muscle_group_table.setGeometry(QtCore.QRect(0, 30, 231, 521))
        self.muscle_group_table.setObjectName("muscle_group_table")
        self.muscle_group_table.setColumnCount(0)
        self.muscle_group_table.setRowCount(0)
        self.exercise_table = QtGui.QTableWidget(Form)
        self.exercise_table.setGeometry(QtCore.QRect(250, 280, 351, 271))
        self.exercise_table.setObjectName("exercise_table")
        self.exercise_table.setColumnCount(0)
        self.exercise_table.setRowCount(0)
        self.workout_table = QtGui.QTableWidget(Form)
        self.workout_table.setGeometry(QtCore.QRect(620, 40, 256, 521))
        self.workout_table.setObjectName("workout_table")
        self.workout_table.setColumnCount(0)
        self.workout_table.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tutorial_button.setText(QtGui.QApplication.translate("Form", "Show Video", None, QtGui.QApplication.UnicodeUTF8))
        self.add_day_button.setText(QtGui.QApplication.translate("Form", "Add Day", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

