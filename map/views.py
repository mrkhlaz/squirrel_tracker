from django.shortcuts import render

from sightings.models import Sighting

def index(request):
    squirrels = Sighting.objects.all()[0:100]
    context = {
            'squirrels': squirrels,
            }
    
    return render(request, 'map/map.html', context)
