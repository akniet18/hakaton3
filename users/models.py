from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

def user_photos_dir(instanse, filename):
    usrnme = f'{instanse.phone}-{instanse.nickname}'
    folder_name = f"{usrnme}/{datetime.today().strftime('%d_%m_%Y')}/{filename}"

    return folder_name


class User(AbstractUser):
	GENDER_MALE = 0
	GENDER_FEMALE = 1
	GENDER_CHOICES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

	avatar = models.ImageField(upload_to=user_photos_dir, null=True, blank=True)
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

	def rating(self):
		sum_r = 0
		rat = 0
		for i in self.rating_array:
			sum_r += i
			rat = sum_r / len(self.rating_array)
		return rat


	def getRating(self):
		return self.user.all()