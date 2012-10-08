from django.db import models


class Instance(models.Model):
    '''
    XXX - An instance of an app deployment - describe in more detail!
    '''
    name = models.CharField(max_length=100)
    desc = models.TextField()
    app_repo_url = models.URLField()

