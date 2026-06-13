from django.contrib import admin
from .models import Flight, Passenger, City

# Register your models here.

admin.site.register(Flight)
admin.site.register(City)
admin.site.register(Passenger)
