# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime, time

from django.contrib.auth.models import User

from django.urls import reverse

class Album(models.Model):
	name = models.CharField(max_length=50)
	artist = models.CharField(max_length=50)
	user  = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('albums:detailAlbum', kwargs={'id': self.id})

class Title(models.Model):
	album = models.OneToOneField(Album, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	duration = models.TimeField(default='00:00')

	def __str__(self):
		return self.title


class Score(models.Model):
	album = models.OneToOneField(Album, on_delete=models.CASCADE, related_name="album")
	user  = models.OneToOneField(User, on_delete=models.CASCADE)
	value = models.DecimalField("Score", default=0, max_digits=2, decimal_places=0)

	def __str__(self):
		return str(self.value)