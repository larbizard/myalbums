# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from albums.models import Album, Score

from albums.albums import AlbumCreationForm, ScoreCreationForm

from django.contrib.auth.models import User

import pdb


# Add album

class AddAlbumFormTest(TestCase):
	def setUp(self):
		self.user = User.objects.create(email="test@test.com", password="user", username="user")

	def test_add_album(self):
		form = AlbumCreationForm(data={'name' : 'AlbumTest', 'artist' : 'ArtistTest', 'user' : self.user})
		self.assertTrue(form.is_valid())

	#def test_score_album(self):
	#	album = Album.objects.create(name='AlbumTest', artist='ArtistTest', user=self.user)
	#	form = ScoreCreationForm(data={'value' : 5, 'album' : album, 'user' : self.user})
	#	pdb.set_trace()
	#	self.assertTrue(form.is_valid())

	#TODO: We should test the albumScore view to see the Ajax Response