from django.conf.urls import patterns, include, url
from django.contrib import admin

from CloudAppExchange.manifest.api import MSMResource


admin.autodiscover()

# Mustard Seed Manifest!
msm_resource = MSMResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CloudAppExchange.views.home', name='home'),
    # url(r'^CloudAppExchange/', include('CloudAppExchange.foo.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(msm_resource.urls)),
)
