from django.contrib import admin
from .models import House

# Register your models here.
# House의 Admin Pannel을 control
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):#admin패널
    #control House model connecting model ~ admin pannel
    fields = ("name", "address", ("price", "pets_allowed"))
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed",
    )
    list_filter = ("price_per_night", "pets_allowed")
    search_fields = ("address__startswith",) #only list or string not tuple
    #exclude = ("price_per_night",)
    list_display_links = ("name", "address")
    list_editable = ("price_per_night","pets_allowed")

