from tastypie.resources import ModelResource
from tastypie import fields

from VirtualResourceController.oms_resources.models import OMSInstance, OMSHost


class OMSHostResource(ModelResource):
    class Meta:
        queryset = OMSHost.objects.all()
        resource_name = 'host'


class OMSInstanceResource(ModelResource):
    host = fields.ForeignKey(OMSHostResource, 'host')

    class Meta:
        queryset = OMSInstance.objects.all()
        resource_name = 'instance'
