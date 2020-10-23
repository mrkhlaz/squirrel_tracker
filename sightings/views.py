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
