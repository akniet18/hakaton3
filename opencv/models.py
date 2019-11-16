from django.db import models


class OpencvModel(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	attnedance = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name