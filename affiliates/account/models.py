from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime
# Create your models here.

"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    affiliate_id = models.AutoField(unique=True)
    address = models.CharField(max_length=200)
    country = CountryField()


class Relation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relationship = CountryField()
    ad_space = models.AutoField(max_length=5, unique=True)


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




