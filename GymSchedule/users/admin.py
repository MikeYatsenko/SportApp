from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import SiteUser


class SiteUserAdmin(UserAdmin):
    model = SiteUser
    list_display = ["username","email"]

admin.site.register(SiteUser,SiteUserAdmin)