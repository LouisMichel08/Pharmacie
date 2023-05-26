from Classes.Medicament import Medicament


class Corticoide(Medicament):
    """
    Class Corticoide
    """
    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "",
                 p_nom_commercial: str = "", p_prix: int = 0, p_categorie: str = "", p_effet_medic: str = ""):
        """
        Constructeur de la classe Coirticoide
        :param p_code_medicament: Code du medicament
        :param p_nom_chimique: Nom chimique du médicament
        :param p_nom_commercial: Nom commercial du médicament
        :param p_prix: Prix du médicament
        :param p_categorie: Catégorie du médicament
        :param p_effet_medic: Effet du médicament
        """
        Medicament.__init__(self, p_code_medicament, p_nom_chimique, p_nom_commercial, p_prix, p_categorie)
        self.Effet_medic = p_effet_medic

    # Méthode magique
    def __str__(self):
        """
        Méthode magique
        :return:
        """
        chaine = Medicament.__str__(self)
        chaine += "\nEffet du médicament : " + self.Effet_medic
        return chaine

