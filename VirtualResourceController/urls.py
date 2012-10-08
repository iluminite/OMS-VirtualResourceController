from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from VirtualResourceController.oms_resources.api import OMSInstanceResource, \
                                                        OMSHostResource

admin.autodiscover()

# setup/register API URL endpoints
v1_api = Api(api_name='v1')
v1_api.register(OMSInstanceResource())   # OMS App Deployment Instance
v1_api.register(OMSHostResource())   # OMS App Deployment Instance


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VirtualResourceController.views.home', name='home'),
    # url(r'^VirtualResourceController/', include('VirtualResourceController.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
