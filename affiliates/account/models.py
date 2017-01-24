from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import random
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_space = models.IntegerField(unique=True)


class Information(models.Model):
    VISITORS_CHOICES = (
        (1000, 'Less than 1000'),
        (5000, '1000 - 10,000'),
        (50000, '10,000 - 100,000'),
        (100000, 'More than 100,000'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    affiliate_type = models.CharField(max_length=300)
    domains = models.CharField(max_length=100)
    is_legal = models.BooleanField(default=None)
    description = models.CharField(max_length=300)
    mediums = models.CharField(max_length=300)
    categories = models.CharField(max_length=300)
    traffic = models.CharField(max_length=300)
    visitors = models.IntegerField(choices=VISITORS_CHOICES)
    product_feed = models.BooleanField()
    feed_fields = models.CharField(max_length=300)
    insertion_order = models.FileField(upload_to='/home/ulises/Linio/django/env/skunk/affiliates/uploads/')
    tax_id = models.FileField(upload_to='/home/ulises/Linio/django/env/skunk/affiliates/uploads/')
    legal_rep = models.FileField(upload_to='/home/ulises/Linio/django/env/skunk/affiliates/uploads/')
    fiscal_add = models.FileField(upload_to='/home/ulises/Linio/django/env/skunk/affiliates/uploads/')
    bank_st = models.FileField(upload_to='/home/ulises/Linio/django/env/skunk/affiliates/uploads/')
    Constitutive = models.FileField(upload_to='/home/ulises/Linio/django/env/skunk/affiliates/uploads/')


"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Relation.objects.create(user=instance)
counter = 1000
@receiver(post_save, sender=User)
def make_adspace(instance):
    q = random.randint(1000,10000)
    p = Relation()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.relation.save()

"""

