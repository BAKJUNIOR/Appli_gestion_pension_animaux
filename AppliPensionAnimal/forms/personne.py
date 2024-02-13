from django.forms import ModelForm

from PensionAnimal.models.Personne import Personne


class Personneform(ModelForm):
    class Meta:
        model = Personne
        fields = ("nom", "prenom", "email", "adresse", "telephone",
                  "code_postal", "ville",  "commentaire")