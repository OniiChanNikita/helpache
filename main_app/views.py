from django.shortcuts import render

# Create your views here.
def main(request):
	return render(request, "main_app/main.html")

def home(request):
	return render(request, "main_app/home.html")