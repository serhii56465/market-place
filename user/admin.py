from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("money", "rating",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("money", "rating",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (("Additional info", {"fields": ("first_name", "last_name", "money", "rating")}),)
    )

