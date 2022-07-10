from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='indexfile'),
    path('business',views.business,name='businessfile'),
    path('entertainment',views.entertainment,name='entertainmentfile'),
    path('sports',views.sports,name='sportsfile'),
    path('politics',views.politics,name='politicsfile'),
    path('nationalnews',views.nationalnews,name='nationalnewsfile'),
    path('startup',views.startup,name='startupfile'),
    path('technology',views.technology,name='technologyfile'),
    path('world',views.world,name='worldfile'),
    path('miscellaneous',views.miscellaneous,name='miscellaneousfile'),
    path('hatke ',views.hatke,name='hatkefile'),
    path('science',views.science,name='sciencefile'),
    path('Automobile',views.Automobile,name='Automobilefile'),

]