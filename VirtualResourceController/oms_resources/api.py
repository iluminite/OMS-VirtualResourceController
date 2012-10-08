from tastypie.resources import ModelResource
from VirtualResourceController.oms_resources.models import Instance


class InstanceResource(ModelResource):
    class Meta:
        queryset = Instance.objects.all()
        resource_name = 'seed'
