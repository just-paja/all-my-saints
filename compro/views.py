import os
import qrcode
import qrcode.image.svg

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import authenticate, login
from loremipsum import Generator

from .models import HollyCompro


def get_holly_text():
    sample_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'sample.txt')
    dictionary_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                   'dictionary.txt')
    sample_txt = open(sample_path, 'r')
    sample = sample_txt.read()

    dictionary_txt = open(dictionary_path, 'r')
    dictionary = dictionary_txt.read().split()
    sample_txt.close()
    dictionary_txt.close()

    g = Generator(sample, dictionary)
    paragraph = g.generate_paragraph()
    return paragraph[2]


def home(request):
    context = {
        'title': 'Reprobus systems',
        'description': 'Welcome to reprobus systems'
    }
    if request.user and request.user.id:
        return redirect('/admin/compro/documentation/add/')
    if request.method == 'POST':
        user = authenticate(username='optimics-anonymous',
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('/admin/compro/documentation/add/')
        else:
            context['failure'] = 'Špatné heslo soryjako.'
    return render(request, 'home.html', context)


def news(request, compro_slug):
    try:
        compro = HollyCompro.objects.get(slug=compro_slug)
    except HollyCompro.DoesNotExist:
        raise Http404
    if request.user.is_superuser:
        return redirect('/admin/compro/hollycomproacquisition/add/?compro=%s' %
                        compro.pk)
    return render(
        request, 'news.html', {
            'compro': compro,
            'date': compro.created_at,
            'description': compro.text,
            'perex': compro.text,
            'text': get_holly_text(),
            'title': compro.title,
        })


def news_qr(request, compro_slug):
    try:
        compro = HollyCompro.objects.get(slug=compro_slug)
    except HollyCompro.DoesNotExist:
        raise Http404
    factory = qrcode.image.svg.SvgImage
    img = qrcode.make('https://%s%s' %
                      (request.META['HTTP_HOST'], compro.get_absolute_url()),
                      image_factory=factory,
                      box_size=64)
    response = HttpResponse(content_type="image/svg+xml")
    img.save(response)
    return response
