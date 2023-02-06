from django.db import models

# Create your models here.


class Polls(models.Model):

    name = models.CharField('Name', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.name
