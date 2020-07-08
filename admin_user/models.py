from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as __


class Profile(models.Model):

    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_OTHER = 'O'

    GENDER_OPTIONS = (
        (GENDER_MALE, __('Male')),
        (GENDER_FEMALE, __('Female')),
        (GENDER_OTHER, __('Other'))
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    phone = models.CharField(max_length=15, unique=True)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True, default=None)