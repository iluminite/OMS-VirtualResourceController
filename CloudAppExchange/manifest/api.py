from tastypie.resources import ModelResource
from CloudAppExchange.manifest.models import MustardSeedManifest


class MSMResource(ModelResource):
    class Meta:
        queryset = MustardSeedManifest.objects.all()
        resource_name = 'seed'
