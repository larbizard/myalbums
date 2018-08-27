# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory

from .models import Album, Title, Score
from .controllers import addAlbum
from .albums import AlbumCreationForm

from .controllers import addAlbum, saveScore

import json
import pdb

@login_required(login_url='/accounts/login/')
def overview(request):
    query_set = Album.objects.all()

    context = {
        "album_list": query_set,
        "title": "Overview des albums",
    }
    return render(request, "index.html", context)


@login_required(login_url='/accounts/login/')
def createAlbum(request):
    form = AlbumCreationForm(request.POST or None)

    if form.is_valid():
        cd = form.cleaned_data
        #now in the object cd, you have the form as a dictionary.
        name = cd.get('name')
        artist = cd.get('artist')
        instance = addAlbum(name, artist, request.user)
        #messages.success(request, "Créé avec succés")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
    	"form": form,
        "title": "Ajouter un album",
    }

    return render(request, "create_album.html", context)


@login_required(login_url='/accounts/login/')
def detailAlbum(request, id=None):
    instance = get_object_or_404(Album, id=id)

    context = {    
        "instance": instance,
    }    
    return render(request, "detail_album.html", context)


@login_required(login_url='/accounts/login/')
def albumScore(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        album_id = request.POST.get('album_id')
        #pdb.set_trace()
        response_data = {}

        album =  Album.objects.filter(id=album_id)[0]

        score = saveScore(value=post_text, album=album, user=request.user)
        
        #score = Score(value=post_text, album=album, user=request.user)
        #score.save()

        response_data['result'] = 'Note sauvegardee avec succes !'
        response_data['postpk'] = score.pk
        response_data['value'] = score.value
        response_data['album'] = score.album
        response_data['user'] = score.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )