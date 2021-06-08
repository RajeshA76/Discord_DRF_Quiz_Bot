from django.db import models
from django.utils.translation import ugettext as _

class Score(models.Model):

    name = models.CharField( ("name"),max_length=100)
    points = models.IntegerField( ("points")) 

    def __str__(self):
        return self.name

