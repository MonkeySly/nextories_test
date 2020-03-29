from django.db import models


class Meuble(models.Model):
    name = models.CharField(max_length=200, null=True)
    length = models.IntegerField(default=0, null=True)
    width = models.IntegerField(default=0, null=True)
    height = models.IntegerField(default=0, null=True)
