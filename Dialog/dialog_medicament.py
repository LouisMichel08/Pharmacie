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
    """
    Cache ou montre les widget appartenant à Antibiotique
    """
    objet.label_antibiotique.setVisible(B)
    objet.label_duree_prise_maximale.setVisible(B)
    objet.lineEdit_duree_prise_max.setVisible(B)

# Permet de cacher ou de montrer les éléments d'analgésique
def cacher_widget_Analgesique(objet, B):
    """
    Cache ou montre les widgets appartenant à Analgésique
    """
    objet.label_analgesique.setVisible(B)
    objet.label_dose_quot_max.setVisible(B)
    objet.lineEdit_dose_quot_max.setVisible(B)

# Permet de cacher ou de montrer les éléments de corticoïde
def cacher_widget_Corticoide(objet, B):
    """
    Cache ou montre les widgets appartenant à Corticoïde
    """
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
        # Cache les labels d'erreurs
        cacher_labels_erreur(self)
        # Affiche les widgets relié aux antibiotiques
        cacher_widget_Antibiotique(self, True)
        # Cache les widgets relié aux analgésiques
        cacher_widget_Analgesique(self, False)
        # Caches les widgets relié aux corticoïdes
        cacher_widget_Corticoide(self, False)
        self.comboBox_categorie.currentIndexChanged.connect(self.afficher_widget)

    # Méthode qui détermine ce que l'interface montre selon le choix de catégorie
    def afficher_widget(self):
        """
        Montre ou cache des widgets selon le choix de l'utilisateur
        """
        # Si l'utilisateur choisi Antibiotique
        if self.comboBox_categorie.currentText() == "Antibiotique":
            cacher_widget_Antibiotique(self, True)
            cacher_widget_Corticoide(self, False)
            cacher_widget_Analgesique(self, False)
        # Si l'utilisateur choisi Analgésique
        elif self.comboBox_categorie.currentText() == "Analgésique":
            cacher_widget_Antibiotique(self, False)
            cacher_widget_Corticoide(self, False)
            cacher_widget_Analgesique(self, True)
        # Si l'utilisateur choisi Corticoïde
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
        # Cache les labels d'erreurs
        cacher_labels_erreur(self)
        # Si l'usager choisi l'option Antibiotique
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

            # Si le code du médicament est invalide
            if medic.Code_medicament == "":
                self.lineEdit_code_medicament.clear()
                self.label_erreur_code_medicament_invalide.setVisible(True)
            # Si le nom chimique est invalide
            if medic.Nom_chimique == "":
                self.lineEdit_nom_chimique.clear()
                self.label_erreur_nom_chimique.setVisible(True)
            # Si le nom commercial est invalide
            if medic.Nom_commercial == "":
                self.lineEdit_nom_commercial.clear()
                self.label_erreur_nom_commercial.setVisible(True)
            # Si le prix est invalides
            if medic.Prix == "":
                self.lineEdit_prix.clear()
                self.label_erreur_prix.setVisible(True)
            # Si tout les éléments sont valides
            if medic.Code_medicament != "" and medic.Nom_chimique != "" and medic.Nom_commercial != ""\
                    and medic.Prix != "" and medic.Duree_prix_max != "":
                Medicament.ls_medicaments.append(medic)
                self.lineEdit_code_medicament.clear()
                self.lineEdit_nom_chimique.clear()
                self.lineEdit_nom_commercial.clear()
                self.lineEdit_prix.clear()
                self.lineEdit_duree_prise_max.clear()
        # Si l'usager choisi l'option Analgésique
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

            # Si le code du médicament est invalide
            if medic.Code_medicament == "":
                self.lineEdit_code_medicament.clear()
                self.label_erreur_code_medicament_invalide.setVisible(True)
            # Si le nom chimique est invalide
            if medic.Nom_chimique == "":
                self.lineEdit_nom_chimique.clear()
                self.label_erreur_nom_chimique.setVisible(True)
            # Si le nom commercial est invalide
            if medic.Nom_commercial == "":
                self.lineEdit_nom_commercial.clear()
                self.label_erreur_nom_commercial.setVisible(True)
            # Si le prix est invalides
            if medic.Prix == "":
                self.lineEdit_prix.clear()
                self.label_erreur_prix.setVisible(True)
            # Si tout les éléments sont valides
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
            # Si le code du médicament est invalide
            if medic.Code_medicament == "":
                self.lineEdit_code_medicament.clear()
                self.label_erreur_code_medicament_invalide.setVisible(True)
            # Si le nom chimique est invalide
            if medic.Nom_chimique == "":
                self.lineEdit_nom_chimique.clear()
                self.label_erreur_nom_chimique.setVisible(True)
            # Si le nom commercial est invalide
            if medic.Nom_commercial == "":
                self.lineEdit_nom_commercial.clear()
                self.label_erreur_nom_commercial.setVisible(True)
            # Si le prix est invalides
            if medic.Prix == "":
                self.lineEdit_prix.clear()
                self.label_erreur_prix.setVisible(True)
            # Si tout les éléments sont valides
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
        # Si le code du médicament est invalide
        if medic.Code_medicament == "":
            self.lineEdit_code_medicament.clear()
            self.label_erreur_code_medicament_existe_pas.setVisible(True)
        # Si le code du médicament est valide, ajoute les éléments aux lineEdit
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


