from django.contrib import admin
from VirtualResourceController.oms_resources.models import OMSInstance, OMSHost

class OMSHostAdmin(admin.ModelAdmin):
    pass

class OMSInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(OMSHost, OMSHostAdmin)
admin.site.register(OMSInstance, OMSInstanceAdmin)
