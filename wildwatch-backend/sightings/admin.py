from django.contrib import admin
from .models import Sighting

# Register your models here.
class SightingAdmin(admin.ModelAdmin):
    fields = ['species', 'location', 'image', 'user']
admin.site.register(Sighting)
