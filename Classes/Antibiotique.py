from Classes.Medicament import Medicament

class Antibiotique(Medicament):
    """
    Classe Antibiotique
    """
    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "",
                 p_nom_commercial: str = "", p_prix: int = 0, p_categorie: str = "", p_duree_prise_max : int =0):
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie)
        self._duree_prix_max = p_duree_prise_max

    # Propriété Duree_prix_max
    def _get_duree_prix_max(self):
        return self._duree_prix_max

    def _set_duree_prix_max(self, v_duree_prix):
        if v_duree_prix > 0:
            self._duree_prix_max = v_duree_prix

    Duree_prix_max = property(_get_duree_prix_max, _set_duree_prix_max)

    # Méthode magique
    def __str__(self):
        """
        Méthode magique str
        :return:
        """
        chaine = Medicament.__str__(self)
        chaine += "\nLa durée maximale de prise du médicament : " + str(self.Duree_prix_max)
        return chaine
