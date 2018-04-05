from django.db import models

# Create your models here.

class Url(models.Model):
    dir = models.CharField(max_length=32)
    def __str__(self):
        return self.dir
