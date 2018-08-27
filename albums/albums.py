from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Album, Title, Score


class AlbumCreationForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ['user',]

        def clean(self):
            cleaned_data = super(AlbumCreationForm, self).clean()


class TitleCreationForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = '__all__'

        def clean(self):
            cleaned_data = super(TitleCreationForm, self).clean()


class ScoreCreationForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'

        def clean(self):
            cleaned_data = super(ScoreCreationForm, self).clean()