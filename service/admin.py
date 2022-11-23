from django.contrib import admin
from .models import Domestic, International, Details, Services
# Register your models here.

@admin.register(Domestic)
class Domesticadmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination']


@admin.register(International)
class Internationaladmin(admin.ModelAdmin):
    list_display = ['id', 'Destination_country', 'origin', 'destination']

@admin.register(Details)
class Detailsadmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination','Destination_country', 'origin', 'destination', 'services',
                    'date', 'price', 'from_whom', 'image']

@admin.register(Services)
class Servicesadmin(admin.ModelAdmin):
    list_display = ['id', 'services', 'date', 'select', 'image']