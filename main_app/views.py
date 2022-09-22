from django.shortcuts import render

from .forms import *
# Create your views here.
def main(request):
	return render(request, "main_app/main.html")

def home(request):
	return render(request, "main_app/home.html")

def log_in(request):
	if request.method == 'POST':
		print("a")
		form = LoginForm(request.POST)
		if form.is_valid():
			print("form login is valid")
	else: form = LoginForm()
	
	return render(request, "main_app/login.html", {"form": form})