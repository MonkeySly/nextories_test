from django.db import models


class Meuble(models.Model):
    name = models.CharField(max_length=200, null=True)
    length = models.IntegerField(default=0, null=True)
    width = models.IntegerField(default=0, null=True)
    height = models.IntegerField(default=0, null=True)

    @property
    def get_volume_in_cm(self):
        return self.length * self.width * self.height

    @property
    def get_volume_in_m(self):
        return self.get_volume_in_cm / 1000000
