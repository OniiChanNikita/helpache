from django.db import models

# Create your models here.

class InfoUserModel(models.Model):
	username = models.CharField(max_length = 255)
	photo = models.ImageField(default=None)