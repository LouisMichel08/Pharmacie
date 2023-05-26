from datetime import date
class Patient:
    """
    Class Patient
    """
    # Attribut de classe
    ls_patients = []
    def __init__(self,p_numero_patient: str = "", p_nom: str = "", p_prenom : str = "",
                 p_date_naiss : date = None, p_list_medic: list = []):
        """
        Constructeur de la classe Patient
        :param p_numero_patient: Numéro du patient
        :param p_nom: Nom du patient
        :param p_prenom: Prénom du patient
        :param p_courriel: Courriel du patient
        :param p_date_naiss: Date de naissance du patient
        :param p_list_medic: Liste des médicaments du patient
        """
        # Attributs d'instance
        self._numero_patient = p_numero_patient
        self._numero_patient = p_numero_patient
        self._nom = p_nom
        self._prenom = p_prenom
        self._date_naiss = p_date_naiss
        self.List_medic = p_list_medic

    # Propriétés
    # Propriété Numero_patient
    def _get_numero_patient(self):
        return self._numero_patient
    def _set_numero_patient(self,v_numero_patient):
        if len(v_numero_patient) == 7 and v_numero_patient.isnumeric() and int(v_numero_patient[0]) % 2 == 0:
            self._numero_patient = v_numero_patient

    Numero_patient = property(_get_numero_patient, _set_numero_patient)
    # Propriété Nom
    def _get_nom(self):
        return self._nom
    def _set_nom(self,v_nom):
        if v_nom.isalpha() and len(v_nom) <= 50:
            self._nom = v_nom
    Nom = property(_get_nom, _set_nom)

    # Propriété Prenom
    def _get_prenom(self):
        return self._prenom
    def _set_prenom(self,v_prenom):
        if v_prenom.isalpha() and len(v_prenom) <= 50:
            self._prenom = v_prenom
    Prenom = property(_get_prenom, _set_prenom)

    # Propriété Courriel
    def _get_courriel(self):
        return self._nom+self._prenom+"@gmail.com"
    Courriel = property(_get_courriel)
    # Propriété Date_naiss
    def _get_date_naiss(self):
        return self._date_naiss
    def _set_date_naiss (self,v_date_naiss):
        if self._calculerAge(v_date_naiss) >= 0:
            self._date_naiss = v_date_naiss
    Date_naiss = property(_get_date_naiss, _set_date_naiss)

    # Méthodes d'instance
    def _calculerAge(self, p_date_naiss : date):
        """
        Calcule l'âge du patient
        :return:
        """
        import datetime
        today = datetime.date.today()
        return today.year - p_date_naiss.year - (
                (today.month, today.day) < (p_date_naiss.month, p_date_naiss.day))

    def estAdule(self):
        """
        Retourne True si le patient est une adulte sinon retourne false
        """
        if self._calculerAge(self._date_naiss) >= 18:
            return True
        else:
            return False

    def afficherMedicaments(self):
        """
        Affiche la liste des médicaments du patient

        """
        for elt_medic in self.List_medic:
            print(elt_medic)

    def ajouterMedicament(self, p_objet_medicament):
        """
        Ajoute le médicament entré en paramètre à la liste des médicaments du patient
        :param : l'objet de la classe Medicament
        """
        self.List_medic.append(p_objet_medicament)
    def supprimerMedicament(self, p_objet_medicament):
        """
        Supprimer un médicament de la liste des médicaments
        :param p_objet_medicament:
        :return:
        """
        self.List_medic.remove(p_objet_medicament)

    # Méthode magique
    def __str__(self):
        """
        Méthode magique str
        """
        chaine = "\n Le numéro du patient : " + self._numero_patient
        chaine += "\n Le nom du patient  : " + self._nom
        chaine += "\n Le prénom du patient : " + self._prenom
        chaine += "\n Le courriel du patient : " + self.Courriel
        return chaine

