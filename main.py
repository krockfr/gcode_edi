import sys
from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore, QtGui
from editeur import Ui_notepad
from coloration_syntaxique import ColorSyntaxSQL


class StartQT4(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setupUi(self)

        # here we connect signals with our slots
        QtCore.QObject.connect(self.ui.boutton_ouvrir, QtCore.SIGNAL("clicked()"), self.afficher_boite_dld_ouvrir)
        QtCore.QObject.connect(self.ui.boutton_enregistrer, QtCore.SIGNAL("clicked()"), self.enregistrer_fichier)
        QtCore.QObject.connect(self.ui.boutton_enregistrer_sous, QtCore.SIGNAL("clicked()"), self.enregistrer_fichier_sous)
        QtCore.QObject.connect(self.ui.boutton_fermer, QtCore.SIGNAL("clicked()"), self.fermer_app)

        #Application de la coloration syntaxique
        self.colorSyntaxSQL = ColorSyntaxSQL(self.ui.editor_window.document())

    #OUVRIR UN FICHIER
    def afficher_boite_dld_ouvrir(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            text = open(self.filename).read()            
            self.ui.editor_window.setText(text)
            

    #ENREGISTRER SOUS
    def enregistrer_fichier_sous(self):        
        fd = QtGui.QFileDialog(self)        
        self.filename = fd.getSaveFileName(self, "Enregistrer programme sous...")
        print "enregistrement fichier " + self.filename
        import codecs
        file = codecs.open(self.filename, 'w', 'utf-8')
        file.write(self.ui.editor_window.toPlainText())
        file.close()
        self.maj_ui()



    #ENREGISTRER
    def enregistrer_fichier(self):
        from os.path import isfile
        if isfile(self.filename):
            import codecs
            file = codecs.open(self.filename, 'w', 'utf-8')
            file.write(self.ui.editor_window.toPlainText())
            file.close()


    #MISE A JOUR DE L'INTERFACE
    def maj_ui(self):
        if self.filename:
           self.ui.label_fichier_ouvert.setText("Fichier Ouvert : " + self.filename)
           self.ui.boutton_enregistrer.setEnabled(True)




#    def affiche(self, chaineunicode):
#       self.edit.append(chaineunicode)
#       self.edit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
 #      QtCore.QCoreApplication.processEvents()

    #FERMER L'APPLICATION
    def fermer_app(self):
        sys.exit()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
