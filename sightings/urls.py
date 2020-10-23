from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.all_sightings),
    #path('add/', views.add, name='add'),
    #path('<int:squirrel_id>/', views.detail, name='detail'),
    #path('stats/', views.stats, name='stats'),
]
