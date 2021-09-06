from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login

from .models import HollyCompro


def home(request):
    context = {
        'title': 'Reprobus systems',
        'description': 'Welcome to reprobus systems'
    }
    if request.method == 'POST':
        user = authenticate(username='optimics-anonymous',
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/admin/compro/documentation/add/')
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
