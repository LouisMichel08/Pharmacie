# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets

from Classes.Medicament import *
from UI_PY.dialog_medicament import *

def cacher_labels_erreur(objet):
    objet.label_erreur_code_medicament_existe_pas.setVisible(False)
    objet.label_erreur_code_medicamen_existe.setVisible(False)
    objet.label_erreur_code_medicament_invalide.setVisible(False)
    objet.label_erreur_nom_chimique.setVisible(False)
    objet.label_erreur_nom_commercial.setVisible(False)
    objet.label_erreur_prix.setVisible(False)
    objet.label_erreur_duree_prise_max.setVisible(False)
    objet.label_erreur_dose_quot_max.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetremedicament(QtWidgets.QDialog, UI_PY.dialog_medicament.Ui_Dialog_Medicament):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetremedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Médicament")
        cacher_labels_erreur(self)

