#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-

from models import Album, Title, Score
from datetime import datetime, timedelta, tzinfo

def addAlbum(name, artist, user):
	album = Album()
	album.name = name
	album.artist = artist
	album.user = user

	album.save()

	return album

def saveScore(value, album, user):
	score = Score()
	score.album = album
	score.user = user
	score.value = value

	score.save()

	return score
