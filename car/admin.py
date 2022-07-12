from django.contrib import admin
from .models import Car, Detail, Detail_Type, Extra
# Register your models here.

class DetailAdminInline(admin.StackedInline):
    model = Detail
    extra = 0

class ExtrasAdminInline(admin.StackedInline):
    model = Extra
    extra = 0

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name','manufacturer_charge']
    search_fields = ['name','manufacturer_charge']
    inlines = [DetailAdminInline,]


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['detail_type','price','quantity','car']
    search_fields = ['detail_type','price','quantity','car']
    inlines = [ExtrasAdminInline,]
    
admin.site.register(Detail_Type)


