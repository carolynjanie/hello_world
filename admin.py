from django.contrib import admin
from .models import smartscan
# Register your models here.
class smartAdmin(admin.ModelAdmin):
	list_display = ('name','tel','license_plate','time_in','time_out','model')

admin.site.register(smartscan,smartAdmin)