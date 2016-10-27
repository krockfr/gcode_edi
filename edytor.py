# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edytor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(800, 646)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.editor_window = QtGui.QTextEdit(self.centralwidget)
        self.editor_window.setGeometry(QtCore.QRect(-7, 87, 821, 511))
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.label_fichier_ouvert = QtGui.QLabel(self.centralwidget)
        self.label_fichier_ouvert.setGeometry(QtCore.QRect(17, 50, 761, 20))
        self.label_fichier_ouvert.setObjectName(_fromUtf8("label_fichier_ouvert"))
        self.boutton_ouvrir = QtGui.QPushButton(self.centralwidget)
        self.boutton_ouvrir.setGeometry(QtCore.QRect(10, 10, 130, 27))
        self.boutton_ouvrir.setObjectName(_fromUtf8("boutton_ouvrir"))
        self.boutton_enregistrer = QtGui.QPushButton(self.centralwidget)
        self.boutton_enregistrer.setGeometry(QtCore.QRect(274, 10, 96, 27))
        self.boutton_enregistrer.setObjectName(_fromUtf8("boutton_enregistrer"))
        self.boutton_fermer = QtGui.QPushButton(self.centralwidget)
        self.boutton_fermer.setGeometry(QtCore.QRect(537, 10, 85, 27))
        self.boutton_fermer.setObjectName(_fromUtf8("boutton_fermer"))
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        notepad.setStatusBar(self.statusbar)

        self.retranslateUi(notepad)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "Editeur Gcode", None))
        self.label_fichier_ouvert.setText(_translate("notepad", "TextLabel", None))
        self.boutton_ouvrir.setText(_translate("notepad", "Ouvrir un fichier", None))
        self.boutton_enregistrer.setText(_translate("notepad", "Enregistrer", None))
        self.boutton_fermer.setText(_translate("notepad", "Fermer", None))

