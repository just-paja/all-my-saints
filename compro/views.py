from django.shortcuts import render
from django.http import Http404
from django.conf import settings

from .models import HollyCompro


def home(request):
    context = {
        'title': 'Reprobus systems',
        'description': 'Welcome to reprobus systems'
    }
    if request.method == 'POST':
        if request.POST['password'] == settings.REPRO_PASSWORD:
            context['success'] = 'Přihlášení úspěšné'
        else:
            context['failure'] = 'Špatné heslo soryjako.'
    return render(request, 'home.html', context)


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
