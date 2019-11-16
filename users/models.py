from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from rest_framework import filters


def user_photos_dir(instanse, filename):
    usrnme = f'{instanse.phone}-{instanse.username}'
    folder_name = f"{usrnme}/{datetime.today().strftime('%d_%m_%Y')}/{filename}"

    return folder_name


class institut(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.name


class cafedra(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	institut = models.ForeignKey(institut, on_delete=models.CASCADE, blank=True, null=True, related_name="cafedra")

	def __str__(self):
		return self.name



class User(AbstractUser):
	GENDER_MALE = 0
	GENDER_FEMALE = 1
	GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

	avatar = models.ImageField(upload_to=user_photos_dir, default="default.png", null=True, blank=True)
	email = models.EmailField(_('email address'), unique=True, blank=True, null=True)
	birth_date = models.DateField(null=True, blank=True)
	location = models.CharField(max_length=30, blank=True, null=True)
	gender = models.SmallIntegerField(choices=GENDER_CHOICES,
                                      null=True, blank=True)
	phone = models.CharField(max_length=30, blank=True, null=True)
	rating_array = ArrayField(models.FloatField(null=True, blank=True, 
                              validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]), null=True ,blank=True, default=list,
                             )
	work_place = models.CharField(max_length=30, blank=True, null=True)
	cafedra = models.ForeignKey(cafedra, on_delete=models.CASCADE, blank=True, null=True, related_name="cafedra")
	job = models.CharField(max_length=30, blank=True, null=True)

	def Allrating(self):
		sum_r = 0
		rat = 0
		for i in self.rating_array:
			sum_r += i
			rat = sum_r / len(self.rating_array)
		return rat


	def comment(self):
		return self.userrat.all()


	def university(self):
		return self.unver.all()


class university(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="unver")
	years = models.CharField(max_length=50, blank=True, null=True)
	spec = models.CharField(max_length=100, blank=True, null=True)
	name = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.user.username