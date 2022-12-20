from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# ! load database into view
from .models import Listing
from listings.choices import price_choices, state_choices, bedroom_choices
# ! Create your views here.

# index means list all the records


def index(request):
    # ! get all data from listing database
    # listings = Listing.objects.all()
    # ! add pagination
    # ! load all the dataset and divide by 3 then we know how many sets of pages
    # ! when user select the page number then GET the page set of data into page_listings
    # ! pass that selected page to template engine

    # ! use context as  "global" variable to hold the dictionary rather than  _ variable value passing

    listings = Listing.objects.order_by('-list_data').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset = Listing.objects.order_by('-list_data')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset.filter(description_icontains=keywords)
    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)
