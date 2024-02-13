
from django.urls import path
from django.views.generic import DetailView
from pyexpat import model

from PensionAnimal.models.Personne import Personne
from PensionAnimal.views import home, personne

urlpatterns = [
    path('', home.index, name='home'),
    #Personne
    path('personnes/', personne.personne_list, name='personnes'),
    path('personnes/create/', personne.CreatePerson.as_view(), name='create_personne'),
    path('personnes/update/<int:pk>', personne.UpdatePerson.as_view(), name='update_personne'),
    path('personnes/<int:pk>/',
         DetailView.as_view(model=Personne, template_name="PensionAnimal/Personne/personne_detail.html"),
         name='detail_personne'),

]
