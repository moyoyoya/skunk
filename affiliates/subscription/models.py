from __future__ import unicode_literals
from affiliates.account.models import User
from django.db import models


# Create your models here.
class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    affiliate_type = models.CharField(blank=True, max_length=300)
    domains = models.CharField(blank=True, max_length=100)
    is_legal = models.BooleanField(default=None)
    description = models.CharField(blank=True, max_length=300)
    mediums = models.CharField(blank=True, max_length=300)
    categories = models.CharField(blank=True, max_length=300)
    traffic = models.CharField(blank=True, max_length=300)
    visitors = models.IntegerField(blank=True)
    product_feed = models.BooleanField(blank=True)
    feed_fields = models.CharField(blank=True, max_length=300)
    insetion_order = models.FileField(blank=True, upload_to='/home/ulises/linio/django/env/skunk/affiliates/uploads/')
    tax_id = models.FileField(blank=True, upload_to='/home/ulises/linio/django/env/skunk/affiliates/uploads/')
    legal_rep = models.FileField(blank=True, upload_to='/home/ulises/linio/django/env/skunk/affiliates/uploads/')
    fiscal_add = models.FileField(blank=True, upload_to='/home/ulises/linio/django/env/skunk/affiliates/uploads/')
    bank_st = models.FileField(blank=True, upload_to='/home/ulises/linio/django/env/skunk/affiliates/uploads/')
    Constittutive = models.FileField(blank=True, upload_to='/home/ulises/linio/django/env/skunk/affiliates/uploads/')