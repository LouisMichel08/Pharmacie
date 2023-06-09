# Louis-Michel Monette

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot, QDate
# Importer la boite de dialogue
import UI_PY.dialog_patient
from PyQt5 import QtWidgets
from Classes.Patient import *
from UI_PY.dialog_patient import *


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

def cacher_labels_erreur(objet):
    """
    Cache les labels d'erreurs
    """
    objet.label_erreur_num_patient_existe.setVisible(False)
    objet.label_errreur_num_patient_existe_pas.setVisible(False)
    objet.label_erreur_num_patient_valider.setVisible(False)
    objet.label_erreur_nom_patient.setVisible(False)
    objet.label_erreur_prenom_patient.setVisible(False)
    objet.label_erreur_date_naiss.setVisible(False)

class Fenetrepatient(QtWidgets.QDialog, UI_PY.dialog_patient.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrepatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Patient")
        # Cache les labels d'erreurs
        cacher_labels_erreur(self)

    # Bouton qui ajoute un patient à la liste des patients
    @pyqtSlot()
    def on_pushButton_Ajouter_patient_clicked(self):
        """
        Gestionnaire d'événement du bouton ajouter Patient
        """
        cacher_labels_erreur(self)

        pat = Patient()

        pat.Numero_patient = self.lineEdit_numero_patient.text()
        pat.Nom = self.lineEdit_nom_patient.text().capitalize()
        pat.Prenom = self.lineEdit_prenom_patient.text().capitalize()
        pat.Date_naiss = self.dateEdit_date_naiss_patient.date()
        # Si le numéro de patient est invalide
        if pat.Numero_patient == "":
            self.lineEdit_numero_patient.clear()
            self.label_erreur_num_patient_valider.setVisible()
        # Si le nom du patient est invalide
        if pat.Nom == "":
            self.lineEdit_nom_patient.clear()
            self.label_erreur_nom_patient.setVisible(True)
        # Si le prenom du patient est invalide
        if pat.Prenom == "":
            self.lineEdit_prenom_patient.clear()
            self.label_erreur_prenom_patient.setVisible(True)
        # Si la date de naissance est invalide
        if pat.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible(True)
        # Si tout les éléments sont valides, ajoute le patient à la liste
        if pat.Numero_patient != "" and pat.Nom != "" and pat.Prenom != "" and pat.Date_naiss != "":
            Patient.ls_patients.append(pat)
            self.lineEdit_numero_patient.clear()
            self.lineEdit_nom_patient.clear()
            self.lineEdit_prenom_patient.clear()
            self.dateEdit_date_naiss_patient.setDate(QDate(2000, 1, 1))

    # Bouton qui supprime un patient de la liste des patients
    @pyqtSlot()
    def on_pushButton_supprimer_patient_clicked(self):
        """
        Gestionnaire d'événement du bouton supprimer Patient
        """
        cacher_labels_erreur(self)

        pat = Patient()

        pat.Numero_patient = self.lineEdit_numero_patient.text()
        pat.Nom = self.lineEdit_nom_patient.text().capitalize()
        pat.Prenom = self.lineEdit_prenom_patient.text().capitalize()
        pat.Date_naiss = self.dateEdit_date_naiss_patient.date()
        # Si le numéro de patient est invalide
        if pat.Numero_patient == "":
            self.lineEdit_numero_patient.clear()
            self.label_erreur_num_patient_valider.setVisible()
        # Si le nom du patient est invalide
        if pat.Nom == "":
            self.lineEdit_nom_patient.clear()
            self.label_erreur_nom_patient.setVisible()
        # Si le prenom du patient est invalide
        if pat.Prenom == "":
            self.lineEdit_prenom_patient.clear()
            self.label_erreur_prenom_patient.setVisible()
        # Si la date de naissance est invalide
        if pat.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible()
        # Si tout les éléments sont valides, supprime le patient de la liste
        if pat.Numero_patient != "" and pat.Nom != "" and pat.Prenom != "" and pat.Date_naiss != "":
            trouve = False
            for elt in Patient.ls_patients:
                if elt.Numero_patient == self.lineEdit_numero_patient.text()\
                    and elt.Nom == self.lineEdit_nom_patient.text().capitalize()\
                    and elt.Prenom == self.lineEdit_prenom_patient.text().capitalize()\
                    and elt.Date_naiss == self.dateEdit_date_naiss_patient.date():
                    trouve = True
                    Patient.ls_patients.remove(elt)
                    break
                if not trouve:
                    self.label_errreur_num_patient_existe_pas.setVisible(True)
                else:
                    self.lineEdit_numero_patient.clear()
                    self.lineEdit_nom_patient.clear()
                    self.lineEdit_prenom_patient.clear()

    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        # fermer la fenêtre
        self.close()
