from django import forms
from . import models
from django.contrib.auth.models import User
import datetime

class AddMeme(forms.ModelForm):
	class Meta:
		model = models.Meme
		fields = ['description', 'image']
