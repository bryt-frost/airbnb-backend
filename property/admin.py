from django.contrib import admin

from property.models import Property, Reservation

admin.site.register([Property, Reservation])
