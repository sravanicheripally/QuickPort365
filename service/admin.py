from django.contrib import admin
from .models import Domestic,International
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Domestic)
class Domesticadmin(admin.ModelAdmin):
    list_display = ['id', 'origin', 'destination']


@admin.register(International)
class Internationaladmin(admin.ModelAdmin):
    list_display = ['id', 'Destination_country', 'origin', 'destination']

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'first_name', 'last_name', 'email']