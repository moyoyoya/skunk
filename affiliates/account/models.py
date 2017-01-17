from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    affiliate_id = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    country = CountryField()
    is_active = models.BooleanField(default=True)
    active_mex = models.BooleanField(default=False)
    active_col = models.BooleanField(default=False)
    active_arg = models.BooleanField(default=False)
    active_per = models.BooleanField(default=False)
    active_chl = models.BooleanField(default=False)
    active_pan = models.BooleanField(default=False)
    active_ven = models.BooleanField(default=False)


class Relation(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    ad_space = models.IntegerField(unique=True)

"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Relation.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.relation.save()

"""

