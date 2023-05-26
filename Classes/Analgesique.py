from Classes.Medicament import Medicament


class Analgesique(Medicament):
    """
    Classe Analgesique
    """
    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "",
                 p_nom_commercial: str = "", p_prix: int = 0, p_categorie: str = "", p_dose_quot_max : int =0):
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie)
        self._dose_quot_max = p_dose_quot_max

    # Propriété Dose_quot_max
    def _get_dose_quot_max(self):
        return self._dose_quot_max

    def _set_dose_quot_max(self,v_dose_quot_max):
        if v_dose_quot_max > 0:
            self._dose_quot_max =v_dose_quot_max

    Dose_quot_max = property(_get_dose_quot_max, _set_dose_quot_max)

    # Méthode magique
    def __str__(self):
        chaine = Medicament.__str__(self)
        chaine += "\nLa dose maximale quotidienne est : "+ str(self._dose_quot_max)
        return chaine


