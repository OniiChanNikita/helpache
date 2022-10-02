from django.db import models

from django.urls import reverse

# Create your models here.

class InfoUserModel(models.Model):
	username = models.CharField(max_length = 255)
	photo = models.ImageField(default=None)

	def __str__(self):
		return self.username

class GuideModel(models.Model):
	creater = models.CharField(max_length = 255)
	title_guide = models.CharField(max_length = 255)
	content_guide = models.TextField()
	categories = models.ForeignKey("CategoriesGuide", on_delete = models.CASCADE)
	date_create = models.DateTimeField(auto_now=True)
	guide_slug = models.CharField(max_length = 50, default = "default")

	def __str__(self):
		return self.title_guide

	def get_abs_url_guide(self):
		return reverse("abs_guide", args = self.guide_slug)

class CategoriesGuide(models.Model):
	categories = models.CharField(max_length = 500)

	def __str__(self):
		return self.categories