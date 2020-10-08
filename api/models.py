from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=40, blank=False, default='')
    email = models.CharField(max_length=50, blank=False, default='')
    gender = models.CharField(max_length=1, default='')