from this import s
from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput
from .models import GuideModel

class LoginForm(forms.Form):
	username_email = forms.CharField(max_length = 255, label = "username")
	password = forms.CharField(widget=PasswordInput(), max_length = 255, label = "password")

class SigninForm(forms.Form):
	email = forms.EmailField(max_length=100, label="email")
	username = forms.CharField(max_length=255, label="username")
	password = forms.CharField(widget=PasswordInput(), max_length=255, label="password")

class AddGuideForm(forms.Form):
	title_guide = forms.CharField(max_length = 500)
	content_guide = forms.CharField(widget=forms.Textarea)
	category = forms.CharField(max_length = 500, label = "New category")
