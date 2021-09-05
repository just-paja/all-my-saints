from django.shortcuts import render
from django.http import Http404

from .models import HollyCompro


def home(request):
    return render(request, 'home.html', {
        'title': 'Reprobus systems',
        'description': 'Welcome to reprobus systems'
    })


def compro(request, compro_slug):
    try:
        compro = HollyCompro.objects.get(slug=compro_slug)
    except HollyCompro.DoesNotExist:
        raise Http404
    return render(request, 'news.html', {
        'title': compro.title,
        'description': compro.text,
        'compro': compro
    })
