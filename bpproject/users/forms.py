from django import forms
from django.forms import ModelForm
from . import models


class Ostads_videos_upload (ModelForm):
    class Meta:
        model = models.Videos
        fields = '__all__'


class Ostads_tamrin_upload (ModelForm):
    class Meta:
        model = models.Tamrin
        fields = '__all__'


class student_tamrin_upload (ModelForm):
    class Meta:
        model = models.Javab
        fields = ['tamrin','number','file']