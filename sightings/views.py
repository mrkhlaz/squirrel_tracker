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
    #sighting = get_object_or_404(___, pk=squirrel_id) #Add index for data
    #context = {
        #'sighting': sighting,
    #}
    #return render(request, 'sightings/detail.html', context)

from collections import Counter
def stats(request):
    squirrels = Sighting.objects.all()
    zones = []
    for sighting in squirrels:
        zones += sighting.hectacre
    zones = Counter(zones)
    mode = zones.most_common(1)
    html = "<html><body>The most common zone for sightings is %s!</body></html>" % mode
    return HttpResponse(html)
