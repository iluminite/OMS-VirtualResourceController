from django.contrib import admin
from CloudAppExchange.manifest.models import MustardSeedManifest

class MSMAdmin(admin.ModelAdmin):
    pass

admin.site.register(MustardSeedManifest, MSMAdmin)
