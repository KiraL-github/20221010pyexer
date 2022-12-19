from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# ! load database into view
from .models import Listing

# Create your views here.

# index means list all the records


def index(request):
    # ! get all data from listing database
    listings = Listing.objects.all()
    # ! use context as  "global" variable to hold the dictionary rather than  _ variable value passing
    paginator = Paginator(listings, 3)
    # ! add paginatation
    page = request.GET.get('page')
    # API/LISTINGS/PAGE?=
    # 係個 input method, 所以用 GET
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)
#  templates/listings/listings


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
