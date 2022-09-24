from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User


from .forms import *
# Create your views here.
def main(request):
	return render(request, "main_app/main.html")

def home(request):
	return render(request, "main_app/home.html")

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