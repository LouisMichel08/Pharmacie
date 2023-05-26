# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import UI_PY.dialog_recherche
from PyQt5 import QtWidgets
from Classes.Fournisseur import *
from Classes.Patient import *


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrerechercher(QtWidgets.QDialog, UI_PY.dialog_recherche.Ui_Dialog_Recherche):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrerechercher, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Rechercher")

    # Méthode qui ajoute les fournisseurs à la listview
    def ajouter_fournisseur(self):
        """
        Ajoute les noms de fournisseur à la comboBox
        """
        Fournisseur.ls_fournisseur = []
        for elt in Fournisseur.ls_fournisseur:
            self.comboBox_nom_fournisseur.addItem(elt)

    @pyqtSlot()
    # Bouton qui affiche le contenu de la listview
    def on_pushButton_afficher_clicked(self):
        """
        Affiche les numéros de patient à la listview
        """
        for elt in self.comboBox_nom_fournisseur:
            self.listView_list_patients_fournisseur.append(elt.Patient.Numero_patient)


