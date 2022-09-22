from django.urls import path
from .views import *

urlpatterns = [
	path("", home, name = "home"),
	path("login/", log_in, name = "login")
]
