from django.contrib import admin

from fitness.models import Events, gallery,event_reg

# Register your models here.

admin.site.register(Events)
admin.site.register(gallery)
admin.site.register(event_reg)