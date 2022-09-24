from django.urls import path
from .views import *

urlpatterns = [
	path("", home, name = "home"),
	path("login/", log_in, name = "login"),
	path("sign_in/", sign_in, name = "signin"),
	path("sign_out/", sign_out, name = "signout"),
]
