from django.contrib import admin
from .models import *

class PLACESAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("PLACE_NAME",)}

class EmployeesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("IIN",)}

class EventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("EVENT_NAME",)}

admin.site.register(PLACES, PLACESAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Events, EventsAdmin)