# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Fri Sep 04 21:27:27 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(956, 571)
        Form.setStyleSheet("QObject#Form{\n"
"\n"
"}")
        self.tutorial_video = phonon.Phonon.VideoPlayer(Form)
        self.tutorial_video.setGeometry(QtCore.QRect(330, 20, 300, 200))
        self.tutorial_video.setObjectName("tutorial_video")
        self.tutorial_button = QtGui.QPushButton(Form)
        self.tutorial_button.setGeometry(QtCore.QRect(330, 230, 75, 23))
        self.tutorial_button.setObjectName("tutorial_button")
        self.add_day_button = QtGui.QPushButton(Form)
        self.add_day_button.setGeometry(QtCore.QRect(480, 240, 75, 23))
        self.add_day_button.setObjectName("add_day_button")
        self.workout_table = QtGui.QTableWidget(Form)
        self.workout_table.setGeometry(QtCore.QRect(690, 40, 256, 521))
        self.workout_table.setObjectName("workout_table")
        self.workout_table.setColumnCount(0)
        self.workout_table.setRowCount(0)
        self.day_delete_button = QtGui.QPushButton(Form)
        self.day_delete_button.setGeometry(QtCore.QRect(650, 240, 31, 21))
        self.day_delete_button.setObjectName("day_delete_button")
        self.muscle_group_combo = QtGui.QComboBox(Form)
        self.muscle_group_combo.setGeometry(QtCore.QRect(0, 10, 181, 22))
        self.muscle_group_combo.setObjectName("muscle_group_combo")
        self.exercise_groupbox = QtGui.QGroupBox(Form)
        self.exercise_groupbox.setGeometry(QtCore.QRect(260, 270, 191, 281))
        self.exercise_groupbox.setObjectName("exercise_groupbox")
        self.verticalLayoutWidget = QtGui.QWidget(self.exercise_groupbox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 191, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.exercise_label = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.exercise_label.setContentsMargins(0, 0, 0, 0)
        self.exercise_label.setObjectName("exercise_label")
        self.exercise_table = QtGui.QTableWidget(Form)
        self.exercise_table.setGeometry(QtCore.QRect(0, 40, 256, 521))
        self.exercise_table.setObjectName("exercise_table")
        self.exercise_table.setColumnCount(0)
        self.exercise_table.setRowCount(0)
        self.day_table = QtGui.QTableWidget(Form)
        self.day_table.setGeometry(QtCore.QRect(510, 270, 161, 291))
        self.day_table.setObjectName("day_table")
        self.day_table.setColumnCount(0)
        self.day_table.setRowCount(0)
        self.rename_button = QtGui.QPushButton(Form)
        self.rename_button.setGeometry(QtCore.QRect(560, 240, 81, 23))
        self.rename_button.setObjectName("rename_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tutorial_button.setText(QtGui.QApplication.translate("Form", "Show Video", None, QtGui.QApplication.UnicodeUTF8))
        self.add_day_button.setText(QtGui.QApplication.translate("Form", "Add Day", None, QtGui.QApplication.UnicodeUTF8))
        self.day_delete_button.setText(QtGui.QApplication.translate("Form", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.exercise_groupbox.setTitle(QtGui.QApplication.translate("Form", "Exercise Description", None, QtGui.QApplication.UnicodeUTF8))
        self.rename_button.setText(QtGui.QApplication.translate("Form", "Rename Day", None, QtGui.QApplication.UnicodeUTF8))

from PySide import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

