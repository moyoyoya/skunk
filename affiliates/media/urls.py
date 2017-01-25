from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from affiliates.account import views as account_views
from . import views as local_views

urlpatterns = [
        url(r'^$', account_views.dashboard, name='dashboard'),
        url(r'^deeplink/$', local_views.deeplink, name='deeplink'),

]