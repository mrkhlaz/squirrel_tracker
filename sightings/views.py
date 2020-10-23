from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Sighting

def all_sightings(request):
    squirrels = Sighting.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/all_sightings.html', context)

#def detail(request, squirrel_id):
    #sighting = get_object_or_404(___, pk=squirrel_id)
    #context = {
        #'sighting': sighting,
    #}
    #return render(request, 'sightings/detail.html', context)
