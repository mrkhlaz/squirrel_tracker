from django.urls import path, re_path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.all_sightings),
    path('add/', views.add_sighting),
    re_path(r'(?P<squirrel_id>[0-9]+[a-zA-Z]-[a-zA-Z]M-[0-9]{4}-[0-9]{2})/$', views.update_sighting),
    #path('stats/', views.stats),
]
