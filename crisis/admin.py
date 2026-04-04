# from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import login, user, hospital, doctor, staff, ambulance, police, complaint, accident, location, department

# Register models
admin.site.register(login)
admin.site.register(user)
admin.site.register(hospital)
admin.site.register(doctor)
admin.site.register(staff)
admin.site.register(ambulance)
admin.site.register(police)
admin.site.register(complaint)
admin.site.register(accident)
admin.site.register(location)
admin.site.register(department)
