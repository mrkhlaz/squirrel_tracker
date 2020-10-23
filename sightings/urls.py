from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.all_sightings),
    #path('add/', views.add, name='add'),
    #re_path(r'(?P<squirrel_id>[0-9]+[a-zA-Z]-[a-zA-Z]M-[0-9]{4}-[0-9]{2})/$', views.article_detail),
    #path('stats/', views.stats, name='stats'),
]
