# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Genre(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Movie(models.Model):
	name = models.CharField(max_length=200)
	year = models.IntegerField()
	genre = models.ForeignKey(Genre, null=True, blank=True)

	def __str__(self):
		return "Movies: {}".format(self.name)