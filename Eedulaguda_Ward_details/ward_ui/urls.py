from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('backend', views.backend, name='backend'),
    path('female', views.female, name='female'),
    path('find',views.find,name = 'find'),
    path('search',views.search,name='search'),
    path('total_male',views.total_male,name='total_male'),
    path('total_female', views.total_female, name='total_female')
]
