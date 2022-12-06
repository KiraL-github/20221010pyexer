from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about')
]

# http://pythonguides.com/get-url-parameters-in-django/
