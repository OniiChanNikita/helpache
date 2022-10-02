from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from .models import *

import random
import string

from .forms import *

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.sample(letters, length))
    print("Random string of length", length, "is:", rand_string)

# Create your views here.
def main(request):
	return render(request, "main_app/main.html")

def home(request):
	if request.user.is_authenticated: return render(request, "main_app/home.html")
	else: return redirect("main")
	

def log_in(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				print("form login is valid")
				User.objects.create_user(username = request.POST["username"], password = request.POST["password"])
				user = authenticate(username = request.POST["username"], password = request.POST["password"])
				if user is not None:
					print("yaaa")
					login(request, user)
					return redirect("main")
		else: form = LoginForm()
		
		return render(request, "main_app/login.html", {"form": form})
	else: return redirect("main")

def sign_in(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				print("form login is valid")
				user = authenticate(username = request.POST["username"], password = request.POST["password"])
				if user is not None:
					print("yaaa")
					login(request, user)
					return redirect("main")
		else: form = LoginForm()

		return render(request, "main_app/sign_in.html", {"form": form})
	else: return redirect("main")

def sign_out(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect("main")

def add_guide(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form_add_guide = AddGuideForm(request.POST)
			if form_add_guide.is_valid():
				print("form add guide is valid")
				
				if GuideModel.objects.get(creater = request.user.username) is None:
					GuideModel.objects.create(creater = request.user.username, title_guide = request.POST["title_guide"],
						content_guide = request.POST["content_guide"], categories = request.POST["categories"], guide_slug = generate_random_string(10))
					
					redirect("guide", slug = "" )

				return redirect("main")
		else: form_add_guide = AddGuideForm()	
	return render(request, "main_app/create_guide.html", {"form_add_guide": form_add_guide})
