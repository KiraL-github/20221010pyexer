from django.shortcuts import render
from .models import Listing

# Create your views here.

# index means list all the records


def index(request):
    # ! get all data from listing database
    listings = Listing.objects.all()
    # ! use context as  "global" variable to hold the dictionary rather than  _ variable value passing
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)
#  templates/listings/listings


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
