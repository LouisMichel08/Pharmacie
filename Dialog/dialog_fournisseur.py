# Louis-Michel Monette

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_fournisseur
from PyQt5 import QtWidgets
from Classes.Fournisseur import *
from Classes.Patient import *

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

# Cache les messages d'erreurs
def cacher_labels_erreur(objet):
    """
    Cache les labels d'erreurs
    """
    objet.label_erreur_code_fournisseur.setVisible(False)
    objet.label_erreur_nom_compagnie.setVisible(False)


class Fenetrefournisseur(QtWidgets.QDialog, UI_PY.dialog_fournisseur.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrefournisseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Fournisseur")
        # Cache les labels qui affichent les messages d'erreurs
        cacher_labels_erreur(self)

    # Méthode qui ajoute les numéros de patient à la comboBox
    def ajouter_num(self):
        """
        Ajoute les numéros de patients à la comboBox
        """
        Patient.ls_patients = []
        for elt in Patient.ls_patients:
            self.comboBox_numero_patient.addItem(elt)

    # Bouton qui permet d'ajouter un patient à la listview
    @pyqtSlot()
    def on_pushButton_ajouter_patient_clicked(self):
        """
        Ajoute un ou plusieurs numéro de patient à la listview
        """
        # Cache les labels qui affichent les messages d'erreurs
        cacher_labels_erreur(self)
        for elt in self.comboBox_numero_patient.currentText():
            self.listView_list_patients.append(elt.__str__())

    # Bouton qui permet de sérialiser les données entrées
    @pyqtSlot()
    def on_pushButton_serialiser_clicked(self):
        """
        Bouton qui ajoute à la liste des fournisseurs et sérialise dans un fichier json
        """
        # Cache les labels qui affichent les messages d'erreurs
        cacher_labels_erreur(self)
        # Instanciation de l'objet Fournisseur
        fourni = Fournisseur()
        # Attributs de l'objet Fournisseur
        fourni.Code_fournisseur = self.lineEdit_code_fournisseur.text()
        fourni.Nom_compagnie = self.lineEdit_nom_compagnie.text().capitalize()
        # Si le code du fournisseur n'est pas valide
        if fourni.Code_fournisseur == "":
            self.lineEdit_code_fournisseur.clear()
            self.label_erreur_code_fournisseur.setVisible(True)
        # Si le nom de la compagnie n'est pas valide
        if fourni.Nom_compagnie == "":
            self.lineEdit_nom_compagnie.clear()
            self.label_erreur_nom_compagnie.setVisible(True)
        # Si le code du fournisseur et le nom de la compagnie sont valides
        if fourni.Code_fournisseur != "" and fourni.Nom_compagnie != "":
            Fournisseur.ls_fournisseur.append(fourni)
            self.lineEdit_code_fournisseur.clear()
            self.lineEdit_nom_compagnie.clear()

        # Si le code et le nom sont valides
        if fourni.Code_fournisseur != "" and fourni.Nom_compagnie != "":
            result = fourni.serialiserFournisseur("." + "/" + "code_fournisseur" + "/" + fourni.Code_fournisseur + "_" + fourni.Nom_compagnie + ".json")

            # Si la sérialisation fonctionne
            if result == 0:
                self.lineEdit_code_fournisseur.clear()
                self.lineEdit_nom_compagnie.clear()

            # Si ne fonctionne pas, affiche les messages d'erreurs
            elif result == 1:
                # Erreur d'écriture du fichier
                self.label_erreur_fichier.setText("Erreur d'écriture dans le fichier")
            else:
                # Erreur d'ouverture du fichier
                self.label_erreur_fichier.setText("Erreur d'ouverture dans le fichier")



