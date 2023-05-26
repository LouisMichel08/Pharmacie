# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_patient
from PyQt5 import QtWidgets

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrepatient(QtWidgets.QDialog, UI_PY.dialog_patient.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrepatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Patient")

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        # fermer la fenêtre
        self.close()
