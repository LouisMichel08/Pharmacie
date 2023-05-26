####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice  gestion de la pharmacie
###  Nom:
###  No étudiant:
###  No Groupe:
###  Description du fichier: Programme principal
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
import PyQt5
from PyQt5 import QtWidgets

#importer les interfaces graphiques
import UI_PY.MainWindow_pharmacie
from PyQt5.QtCore import pyqtSlot
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate
# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from Dialog.dialog_fournisseur import Fenetrefournisseur
from Dialog.dialog_medicament import Fenetremedicament
from Dialog.dialog_patient import Fenetrepatient
from Dialog.dialog_rechercher import Fenetrerechercher


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

########################################################
###### DÉFINITIONS DE LA CLASSE fenetrePrincipale ######
########################################################
# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)

class fenetrePrincipale(QtWidgets.QMainWindow,UI_PY.MainWindow_pharmacie.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow_pharmacie : Ma classe générée avec QtDesigner
    """
    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et MainWindow_pharmacie.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(fenetrePrincipale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion de la pharmacie")
    # Gestionnaire d'événement du bouton Patient
    @pyqtSlot()
    def on_pushButton_patient_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetrepatient()
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()
    # gastionnaire d'événement du bouton Médicament
    @pyqtSlot()
    def on_pushButton_medicament_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetremedicament()
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_fournisseur_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetrefournisseur()
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_recherche_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetrerechercher()
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()
#################################
###### PROGRAMME PRINCIPAL ######
#################################
# Créer le main qui lance la fenêtre de Qt
def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetrePrincipale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()
