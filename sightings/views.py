from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Sighting
from .forms import SightingForm

def all_sightings(request):
    squirrels = Sighting.objects.all()
    context = {
            'squirrels': squirrels,
            }
    return render(request, 'sightings/all_sightings.html', context)

<<<<<<< HEAD
def add_sighting(request):
    if request.method == 'POST':
	form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings")
    else:
	form = SightingForm()

    context = {
            'form':form
            }
    return render(request, 'sightings/add_sighting.html', context)

def update_sighting(request, squirrel_id):
    sighting = get_object_or_404(Sighting, unique_squirrel_id = squirrel_id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        form = SightingForm(instance=sighting)
    
    context = {
            'form':form
            }

    return render(request, 'sightings/update_sighting.html', context)

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
=======
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
>>>>>>> 1d566e5c2554d0c618c7ab8b4e2ea07658faf9af
