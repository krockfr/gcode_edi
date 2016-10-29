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
        notepad.resize(800, 600)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.boutton_ouvrir = QtGui.QPushButton(self.centralwidget)
        self.boutton_ouvrir.setObjectName(_fromUtf8("boutton_ouvrir"))
        self.gridLayout.addWidget(self.boutton_ouvrir, 0, 0, 1, 1)
        self.boutton_enregistrer_sous = QtGui.QPushButton(self.centralwidget)
        self.boutton_enregistrer_sous.setObjectName(_fromUtf8("boutton_enregistrer_sous"))
        self.gridLayout.addWidget(self.boutton_enregistrer_sous, 0, 1, 1, 1)
        self.boutton_enregistrer = QtGui.QPushButton(self.centralwidget)
        self.boutton_enregistrer.setEnabled(False)
        self.boutton_enregistrer.setObjectName(_fromUtf8("boutton_enregistrer"))
        self.gridLayout.addWidget(self.boutton_enregistrer, 0, 2, 1, 1)
        self.boutton_fermer = QtGui.QPushButton(self.centralwidget)
        self.boutton_fermer.setObjectName(_fromUtf8("boutton_fermer"))
        self.gridLayout.addWidget(self.boutton_fermer, 0, 3, 1, 1)
        self.label_fichier_ouvert = QtGui.QLabel(self.centralwidget)
        self.label_fichier_ouvert.setText(_fromUtf8(""))
        self.label_fichier_ouvert.setObjectName(_fromUtf8("label_fichier_ouvert"))
        self.gridLayout.addWidget(self.label_fichier_ouvert, 1, 0, 1, 4)
        self.editor_window = QtGui.QTextEdit(self.centralwidget)
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.gridLayout.addWidget(self.editor_window, 2, 0, 1, 4)
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        notepad.setStatusBar(self.statusbar)
        self.actionOuvrir = QtGui.QAction(notepad)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionEnregistrer = QtGui.QAction(notepad)
        self.actionEnregistrer.setObjectName(_fromUtf8("actionEnregistrer"))
        self.actionEnregistrer_sous = QtGui.QAction(notepad)
        self.actionEnregistrer_sous.setObjectName(_fromUtf8("actionEnregistrer_sous"))
        self.actionQuitter = QtGui.QAction(notepad)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionEnregistrer_sous)
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(notepad)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "Editeur Gcode", None))
        self.boutton_ouvrir.setText(_translate("notepad", "Ouvrir un fichier", None))
        self.boutton_enregistrer_sous.setText(_translate("notepad", "Enregistrer sous", None))
        self.boutton_enregistrer.setText(_translate("notepad", "Enregistrer", None))
        self.boutton_fermer.setText(_translate("notepad", "Fermer", None))
        self.menuFichier.setTitle(_translate("notepad", "Fichier", None))
        self.actionOuvrir.setText(_translate("notepad", "Ouvrir", None))
        self.actionEnregistrer.setText(_translate("notepad", "Enregistrer", None))
        self.actionEnregistrer_sous.setText(_translate("notepad", "Enregistrer sous", None))
        self.actionQuitter.setText(_translate("notepad", "Quitter", None))

