from django.db import models
from django.conf import settings



class Rating(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="auhtor")
	rating = models.FloatField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,related_name="user")


	def __str__(self):
		return self.author.username