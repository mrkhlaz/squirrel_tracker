from django.shortcuts import render

from sightings.models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()[0:100]
    context = {
            'squirrels': squirrels,
            }
    
    return render(request, 'map/map.html', context)
