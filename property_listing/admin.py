from django.contrib import admin
from property_listing.models import PropertyListing
# Register your models here.

class property_linsting_admin(admin.ModelAdmin):

    list_display=('name','location','price','property_type','status')


admin.site.register(PropertyListing,property_linsting_admin)