from django.shortcuts import render


def index(request):
    selected = "home"
    return render(request, 'PensionAnimal/Home.html', locals())