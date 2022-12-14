from django.urls import path
from .views import *

urlpatterns = [
	path("", home, name = "home"),
	path("/guide/<slug:guide_slug")
	path("login/", log_in, name = "login"),
	path("sign_in/", sign_in, name = "signin"),
	path("sign_out/", sign_out, name = "signout"),
	path("create_guide/", add_guide, name = "create_guide"),
]
