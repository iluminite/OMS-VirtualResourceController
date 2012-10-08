from django.conf.urls import patterns, include, url
from django.contrib import admin

from VirtualResourceController.oms_resources.api import InstanceResource


admin.autodiscover()

# OMS App Deployment Instance
instance_resource = InstanceResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VirtualResourceController.views.home', name='home'),
    # url(r'^VirtualResourceController/', include('VirtualResourceController.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(instance_resource.urls)),
)
