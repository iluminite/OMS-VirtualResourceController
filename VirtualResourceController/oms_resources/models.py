from django.db import models
#from django_extensions.db.fields import UUIDField


class OMSHost(models.Model):
    '''
    an OMS Host is one that has been registered with a user's VRC
    '''
#   guid = UUIDField(version=4, blank=True)
    name = models.CharField(max_length=50)
    ip_address = models.IPAddressField()
    mac_address = models.CharField(max_length=25)


OMS_PROJECT_CHOICES = (
    ('registry', 'OMS-RegistryServer'),
    ('resource', 'OMS-ResourceServer'),
    ('pds', 'OMS-PDS'),
    ('sandbox', 'OMS-Sandbox'),
    ('exchange', 'OMS-CloudAppExchange'),
    ('vrc', 'OMS-VirtualResourceController'),
)


class OMSInstance(models.Model):
    '''
    XXX - An instance of an oms app deployment - describe in more detail!
    '''
#   guid = UUIDField(version=4, blank=True)
    name = models.CharField(max_length=50)   # XXX - a limit like this needs to be documented or otherwise made uniform, this limit affects a value the user could define/set in a config.ini
    project = models.CharField(max_length=50, choices=OMS_PROJECT_CHOICES)
    host = models.ForeignKey(OMSHost)
