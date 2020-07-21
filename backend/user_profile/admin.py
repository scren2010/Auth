from django.contrib import admin

from backend.user_profile.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',]


admin.site.register(Profile, ProfileAdmin)
