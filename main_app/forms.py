from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from .models import GuideModel

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 255, label = "username")
	password = forms.CharField(widget=PasswordInput(), max_length = 255, label = "password")

class AddGuideForm(forms.Form):
	