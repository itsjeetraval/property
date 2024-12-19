from django.shortcuts import render
from property_listing.models import *
from django.db.models import Min,Max,Q

def home(request):

    min_price = PropertyListing.objects.all().aggregate(Min('price'))['price__min']
    max_price = PropertyListing.objects.all().aggregate(Max('price'))['price__max']
    

    default_price = round((min_price + max_price) / 2)
    price_value=default_price

    property_data = PropertyListing.objects.all()

    if request.method == "POST":
        property_type = request.POST.get('property_type')
        locations = request.POST.getlist('locations') 
        status = request.POST.get('status')
        price_value = request.POST.get('price_value')


        filter_conditions = Q()

        if property_type:
            filter_conditions &= Q(property_type=property_type)
        if locations:
            filter_conditions &= Q(location__in=locations)
        if status:
            filter_conditions &= Q(status=status)
        if price_value:
            
            price_value = float(price_value)
            filter_conditions &= Q(price__lte=price_value)
 
        property_data = PropertyListing.objects.filter(filter_conditions)


    data = {
        'pro_data': property_data,
        'min_price': min_price,
        'max_price': max_price,  
        'price_value':price_value     
    }

    return render(request, "index.html", data)