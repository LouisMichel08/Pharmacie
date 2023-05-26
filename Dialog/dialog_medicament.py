# Louis-Michel Monette

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets

from Classes.Medicament import *
from UI_PY.dialog_medicament import *
from Classes.Antibiotique import *
from Classes.Analgesique import *
from Classes.Corticoide import *

# Cache les messages d'erreurs
def cacher_labels_erreur(objet):
    objet.label_erreur_code_medicament_existe_pas.setVisible(False)
    objet.label_erreur_code_medicamen_existe.setVisible(False)
    objet.label_erreur_code_medicament_invalide.setVisible(False)
    objet.label_erreur_nom_chimique.setVisible(False)
    objet.label_erreur_nom_commercial.setVisible(False)
    objet.label_erreur_prix.setVisible(False)
    objet.label_erreur_duree_prise_max.setVisible(False)
    objet.label_erreur_dose_quot_max.setVisible(False)

# Permet de cacher ou de montrer les éléments d'antibiotique
def cacher_widget_Antibiotique(objet, B):
    objet.label_antibiotique.setVisible(B)
    objet.label_duree_prise_maximale.setVisible(B)
    objet.lineEdit_duree_prise_max.setVisible(B)

# Permet de cacher ou de montrer les éléments d'analgésique
def cacher_widget_Analgesique(objet, B):
    objet.label_analgesique.setVisible(B)
    objet.label_dose_quot_max.setVisible(B)
    objet.lineEdit_dose_quot_max.setVisible(B)

# Permet de cacher ou de montrer les éléments de corticoïde
def cacher_widget_Corticoide(objet, B):
    objet.label_corticoide.setVisible(B)
    objet.label_effet_medicament.setVisible(B)
    objet.comboBox_effet_medicament.setVisible(B)


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
        cacher_widget_Antibiotique(self, True)
        cacher_widget_Analgesique(self, False)
        cacher_widget_Corticoide(self, False)
        self.comboBox_categorie.currentIndexChanged.connect(self.afficher_widget)

    # Méthode qui détermine ce que l'interface montre selon le choix de catégorie
    def afficher_widget(self):
        if self.comboBox_categorie.currentText() == "Antibiotique":
            cacher_widget_Antibiotique(self, True)
            cacher_widget_Corticoide(self, False)
            cacher_widget_Analgesique(self, False)
        elif self.comboBox_categorie.currentText() == "Analgésique":
            cacher_widget_Antibiotique(self, False)
            cacher_widget_Corticoide(self, False)
            cacher_widget_Analgesique(self, True)
        else:
            cacher_widget_Antibiotique(self, False)
            cacher_widget_Corticoide(self, True)
            cacher_widget_Analgesique(self, False)

    # Bouton qui ajoute un patient à la liste des patients
    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'événement du bouton ajouter Patient
        """
        cacher_labels_erreur(self)
        if self.comboBox_categorie.currentText() == "Antibiotique":

            medic = Medicament()

            medic.Code_medicament = self.lineEdit_code_medicament.text()
            medic.Nom_chimique = self.lineEdit_nom_chimique.text().capitalize()
            medic.Nom_commercial = self.lineEdit_nom_commercial.text().capitalize()
            try:
                medic.Prix = self.lineEdit_prix.text()
            except:
                self.label_erreur_prix.setVisible(True)

            try:
                medic.Duree_prix_max = self.lineEdit_duree_prise_max.text()
            except:
                self.label_erreur_duree_prise_max.setVisible(True)


            if medic.Code_medicament == "":
                self.lineEdit_code_medicament.clear()
                self.label_erreur_code_medicament_invalide.setVisible()

            if medic.Nom_chimique == "":
                self.lineEdit_nom_chimique.clear()
                self.label_erreur_nom_chimique.setVisible()

            if medic.Nom_commercial == "":
                self.lineEdit_nom_commercial.clear()
                self.label_erreur_nom_commercial.setVisible()

            if medic.Prix == "":
                self.lineEdit_prix.clear()
                self.label_erreur_prix.setVisible()

            if medic.Code_medicament != "" and medic.Nom_chimique != "" and medic.Nom_commercial != ""\
                    and medic.Prix != "" and medic.Duree_prix_max != "":
                Medicament.ls_medicaments.append(medic)
                self.lineEdit_code_medicament.clear()
                self.lineEdit_nom_chimique.clear()
                self.lineEdit_nom_commercial.clear()
                self.lineEdit_prix.clear()
                self.lineEdit_duree_prise_max.clear()

        elif self.comboBox_categorie.currentText() == "Analgésique":
            medic = Medicament()

            medic.Code_medicament = self.lineEdit_code_medicament.text()
            medic.Nom_chimique = self.lineEdit_nom_chimique.text().capitalize()
            medic.Nom_commercial = self.lineEdit_nom_commercial.text().capitalize()
            try:
                medic.Prix = self.lineEdit_prix.text()
            except:
                self.label_erreur_prix.setVisible(True)

            try:
                medic.Dose_quot_max = self.lineEdit_dose_quot_max.text()
            except:
                self.label_erreur_dose_quot_max.setVisible(True)


            if medic.Code_medicament == "":
                self.lineEdit_code_medicament.clear()
                self.label_erreur_code_medicament_invalide.setVisible()

            if medic.Nom_chimique == "":
                self.lineEdit_nom_chimique.clear()
                self.label_erreur_nom_chimique.setVisible()

            if medic.Nom_commercial == "":
                self.lineEdit_nom_commercial.clear()
                self.label_erreur_nom_commercial.setVisible()

            if medic.Prix == "":
                self.lineEdit_prix.clear()
                self.label_erreur_prix.setVisible()

            if medic.Code_medicament != "" and medic.Nom_chimique != "" and medic.Nom_commercial != ""\
                    and medic.Prix != "" and medic.Dose_quot_max != "":
                Medicament.ls_medicaments.append(medic)
                self.lineEdit_code_medicament.clear()
                self.lineEdit_nom_chimique.clear()
                self.lineEdit_nom_commercial.clear()
                self.lineEdit_prix.clear()
                self.lineEdit_dose_quot_max.clear()

        else:
            medic = Medicament()

            medic.Code_medicament = self.lineEdit_code_medicament.text()
            medic.Nom_chimique = self.lineEdit_nom_chimique.text().capitalize()
            medic.Nom_commercial = self.lineEdit_nom_commercial.text().capitalize()
            try:
                medic.Prix = self.lineEdit_prix.text()
            except:
                self.label_erreur_prix.setVisible(True)
            medic.Effet_medic = self.comboBox_effet_medicament.currentText()

            if medic.Code_medicament == "":
                self.lineEdit_code_medicament.clear()
                self.label_erreur_code_medicament_invalide.setVisible()

            if medic.Nom_chimique == "":
                self.lineEdit_nom_chimique.clear()
                self.label_erreur_nom_chimique.setVisible()

            if medic.Nom_commercial == "":
                self.lineEdit_nom_commercial.clear()
                self.label_erreur_nom_commercial.setVisible()

            if medic.Prix == "":
                self.lineEdit_prix.clear()
                self.label_erreur_prix.setVisible()

            if medic.Code_medicament != "" and medic.Nom_chimique != "" and medic.Nom_commercial != ""\
                    and medic.Prix != "" and medic.Duree_prix_max != "":
                Medicament.ls_medicaments.append(medic)
                self.lineEdit_code_medicament.clear()
                self.lineEdit_nom_chimique.clear()
                self.lineEdit_nom_commercial.clear()
                self.lineEdit_prix.clear()

     # Bouton cherche un patient selon les données entrées
    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        medic = Medicament()

        medic.Code_medicament = self.lineEdit_code_medicament.text()
        medic.Nom_chimique = self.lineEdit_nom_chimique.text().capitalize()
        medic.Nom_commercial = self.lineEdit_nom_commercial.text().capitalize()
        medic.Prix = self.lineEdit_prix.text()
        medic.Duree_prix_max = self.lineEdit_duree_prise_max.text()
        medic.Dose_quot_max = self.lineEdit_dose_quot_max.text()
        medic.Effet_medic = self.comboBox_effet_medicament.currentText()

        if medic.Code_medicament == "":
            self.lineEdit_code_medicament.clear()
            self.label_erreur_code_medicament_existe_pas.setVisible(True)

        if medic.Code_medicament != "":
            for elt in Medicament.ls_medicaments:
                if elt.Code_medicament == self.lineEdit_code_medicament.text():
                    self.lineEdit_code_medicament.append(elt.Code_medicament)
                    self.lineEdit_nom_chimique.append(elt.Nom_chimique)
                    self.lineEdit_nom_commercial.append(elt.Nom_commercial)
                    self.lineEdit_prix.append(elt.Prix)
                    self.lineEdit_duree_prise_max.append(elt.Duree_prix_max)
                    self.lineEdit_dose_quot_max.append(elt.Dose_quot_max)
                    self.comboBox_effet_medicament.append(elt.Effet_medic)


