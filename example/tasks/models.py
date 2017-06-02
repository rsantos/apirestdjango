# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='tasks', null=True)

    def __str__(self):
        return "%s" % self.title