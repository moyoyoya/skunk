from django.contrib import admin
from .models import Profile, Relation


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['user']}),
        ('Date information',  {'fields': ['affiliate_id', 'company_name', 'is_active'], 'classes': ['collapse']}),
    ]


admin.site.register(Profile, ProfileAdmin)