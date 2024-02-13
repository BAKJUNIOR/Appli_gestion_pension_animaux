from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from AppliPensionAnimal.forms.personne import Personneform
from PensionAnimal.models.Personne import Personne


def personne_list(request):
    selected = "personnes"
    personne_list = Personne.objects.all()

    #pagination : 10 élementspar page
    paginator = Paginator(personne_list.order_by('-date_mise_a_jour'),10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        personne_list = paginator.page(page)
    except EmptyPage:
        # si on dépasse la limite de page , on prend la derniere
        personne_list = paginator.page(paginator.num_pages())
    return render(request, 'PensionAnimal/Personne/personne_list.html', locals() )


class CreatePerson(CreateView):
    model = Personne
    form_class = Personneform
    template_name = "PensionAnimal/Personne/personne_Form.html"

    def get_success_url(self):
        return  reverse_lazy("detail_personne", kwargs={"pk": self.object.id})


class UpdatePerson(UpdateView):
    model = Personne
    form_class = Personneform
    template_name = "PensionAnimal/Personne/personne_Form.html"

    def get_success_url(self):
        return reverse_lazy("detail_personne",kwargs={"pk": self.object.id})