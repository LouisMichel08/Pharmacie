class Medicament :
    """
    Classe Medicament
    """
    # Attribut de classe
    ls_medicaments = []
    def __init__(self, p_code_medicament: str = "", p_nom_chimique: str = "",
                 p_nom_commercial: str = "", p_prix: int = 0, p_categorie: str = ""):
        """
        Constructeur de la classe Medicament
        :param p_code_medicament: Code du médicament
        :param p_nom_chimique: Nom chimique du médicament
        :param p_nom_commercial: Nom commercial du médicament
        :param p_prix: Prix du médicament
        :param p_categorie: Catégorie du médicament
        """
        # Attributs privés
        self._code_medicament = p_code_medicament
        self._nom_chimique = p_nom_chimique
        self._nom_commercial = p_nom_commercial
        self._prix = p_prix
        # Attribut public
        self.Categorie = p_categorie


    # Propriétés
    # Propriété Code_medicament
    def _get_code_medicament(self):
        return self._code_medicament
    def _set_code_medicament(self, v_code_medicament):
        if len(v_code_medicament) == 6 and v_code_medicament[0:3].isalpha()\
                and v_code_medicament[3:6].isnumeric():
            self._code_medicament = v_code_medicament
    Code_medicament = property(_get_code_medicament, _set_code_medicament)
    # Propriété Nom_chimique
    def _get_nom_chimique(self):
        return self._nom_commercial
    def _set_nom_chimique(self,v_nom_chimique):
        if len(v_nom_chimique) <= 50 and v_nom_chimique.isalpha():
            self._nom_chimique = v_nom_chimique
    Nom_chimique = property(_get_nom_chimique, _set_nom_chimique)
    # Propriété nom commercial
    def _get_nom_commercial(self):
        return self._nom_commercial
    def _set_nom_commercial(self,v_nom_commercial):
        if len(v_nom_commercial) <= 50 and v_nom_commercial.isalpha():
            self._nom_commercial = v_nom_commercial
    Nom_commercial = property(_get_nom_commercial, _set_nom_commercial)
    # Propriété Prix
    def _get_prix(self):
        return self._prix
    def _set_prix(self,v_prix):
        if v_prix >= 5  and v_prix <=100:
            self._prix = v_prix
    Prix = property(_get_prix, _set_prix)

    # Méthode magique
    def __str__(self):
        """
        Méthode magique de la classe Medicament
        :return:
        """
        chaine = "\nLe code du médicament est: " + self._code_medicament
        chaine += "\nLe nom chimique est : "+ self._nom_chimique
        chaine += "\nLe nom commercial : " + self._nom_commercial
        chaine += "\nLe prix du médicament : " + str(self._prix)
        chaine += "\nLa catégorie du médicament :"+str(self.Categorie)
        return chaine


class Patient:
    pass