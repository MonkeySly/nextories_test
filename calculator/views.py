from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from calculator.models import Meuble


def index(request):

    context = {}
    if Meuble.objects.count() > 0:
        context['meubles'] = Meuble.objects.all()
        context['total_volume'] = sum(x.get_volume_in_m for x in context.get('meubles'))

    return TemplateResponse(request, 'main.jhtml', context=context)


def compute(request):

    if request.method == 'POST':
        split_list = request.body.decode().split('&')[1:]
        data = {}
        for x in split_list:
            data[x.split('=')[0]] = x.split('=')[1]

        new_meuble, created = Meuble.objects.get_or_create(name=data.get('name'),
                                                           length=int(data.get('length')),
                                                           width=int(data.get('width')),
                                                           height=int(data.get('height')))
        if not created:
            # I should pop an error here but... lazy right now
            pass
        return HttpResponseRedirect(reverse('index'))

