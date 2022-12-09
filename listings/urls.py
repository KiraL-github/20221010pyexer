from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    # int:integer or str:string eg:a34hg7
    path('search', views.search, name='search'),
]
