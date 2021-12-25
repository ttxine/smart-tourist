from django.contrib import admin

from contact.models import TouristApplication, EmployerApplication, Collaboration

admin.site.register(TouristApplication)
admin.site.register(EmployerApplication)
admin.site.register(Collaboration)
