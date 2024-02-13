from django.core.validators import RegexValidator
from django.db import models


class Personne(models.Model):
    date_mise_a_jour = models.DateField(verbose_name= "Date de mise a jour", auto_now=True)   #permet de trier les liste pas date de mise a jour
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=150)
    adresse = models.CharField(max_length=200)
    code_postal_regex = RegexValidator(regex="^[0-9]*$", message= "Veuillez entrer un code postal valide") #Pour appliquer le bon format d'un code postal peut juste contenu de 0 a 9 le code
    code_postal = models.CharField(max_length=5, validators=[code_postal_regex]) #appelle de regex créer
    ville = models.CharField(max_length=100)
    telephone_regex = RegexValidator(regex="[0-9]{10}", message= "Veuillez entrer un numéro de télephone valide.")
    telephone = models.CharField(max_length=10, validators=[telephone_regex])
    date_inscription = models.DateField(verbose_name= "Date d'inscription", auto_now_add=True)   #permet la date du moment
    commentaire = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def get_adresse_complete_str(self):
        return f"{self.adresse}\n {self.code_postal}{self.ville}"






