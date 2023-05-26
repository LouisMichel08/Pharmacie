from Classes.Medicament import Medicament
from Classes.Medicament import Patient
import jsonpickle

class Fournisseur:
    # Attributs de classe
    nb_fournisseur = 0
    ls_fournisseur = []
    def __init__(self, p_code_fournisseur : str = "", p_nom_compagnie: str = "",
                 p_ls_patient: list = []):
        """
        Constructeur de la classe Fournisseur
        :param p_code_fournisseur : Code du fournisseur
        :param p_nom_compagnie : Nom de la compagnie
        :param p_lst_patient : Liste des patients qui achètent des médicaments
        chez ce fournisseur
        """
        # Attribut d'instance
        self._code_fournisseur = p_code_fournisseur
        self._nom_compagnie = p_nom_compagnie
        self.Ls_patient = p_ls_patient

    # Propriété
    # Propiété Code_fournisseur
    def _get_code_fournisseur(self):
        return self._code_fournisseur
    def _set_code_fournisseur(self,v_code_fournisseur):
        if len(v_code_fournisseur) == 7 and v_code_fournisseur[0].isalpha() and \
                v_code_fournisseur[1]=="-" and v_code_fournisseur[2:8].isalnum():
            self._code_fournisseur = v_code_fournisseur

    Code_fournisseur = property(_get_code_fournisseur, _set_code_fournisseur)

    # Proriété Nom_compagnie
    def _get_nom_compagnie(self):
        return self._nom_compagnie
    def _set_nom_compagnie(self,v_nom_compagnie):
        if len(v_nom_compagnie) <= 30 and v_nom_compagnie.isalnum():
            self._nom_compagnie = v_nom_compagnie
    Nom_compagnie = property(_get_nom_compagnie,_set_nom_compagnie)

    # Méthode magique __str__
    def __str__(self):
        chaine = "\n Le code du fournisseur : " + self._code_fournisseur
        chaine += "\n La nom du fournisseur : " + self._nom_compagnie
        return chaine
    # Méthode sérialiser
    def serialiserFournisseur(self, p_nom_fichier):
        jsonchaine = jsonpickle.encode(self)
        with open (p_nom_fichier, "w") as File:
            File.write(jsonchaine)
        pass
    # Méthode désirialiser
    def deserialiserFournisseur(self,p_nom_fichier):
        with open(p_nom_fichier, "r") as file:
            jsonchaine = file.readline()
        self = jsonpickle.decode(jsonchaine)

    # Ajouter médicament au patient
    def ajouterMedicamentPatient(self, p_numero_patient, p_objet_medicament: Medicament):
        for elt in self.Ls_patient:
            if elt.Numero_patient == p_numero_patient:
                elt.List_medic.append(p_objet_medicament)

    @classmethod
    def afficherLstFournisseur(cls):
        for elt_fournisseur in Fournisseur.ls_fournisseur:
            print(elt_fournisseur)

