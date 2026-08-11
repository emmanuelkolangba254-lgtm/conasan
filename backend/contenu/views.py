# Create your views here.
from django.shortcuts import render
from .models import Actualite, Partenaire, StructureSanitaire


def accueil(request):

    actualites = Actualite.objects.all().order_by('-date_publication')[:3]

    partenaires = Partenaire.objects.all()

    structures = StructureSanitaire.objects.all()[:6]

    context = {
        'actualites': actualites,
        'partenaires': partenaires,
        'structures': structures,
    }

    return render(request, 'index.html', context)
