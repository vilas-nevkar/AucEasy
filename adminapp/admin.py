from django.contrib import admin

from .models import AdminUser, Country, City, State, Area

admin.site.register(AdminUser)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Area)