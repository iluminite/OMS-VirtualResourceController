from django.db import models


class MustardSeedManifest(models.Model):
    '''
    The Mustard Seed at the heart of it all!
    '''
    name = models.CharField(max_length=100)
    desc = models.TextField()
    app_repo_url = models.URLField()

