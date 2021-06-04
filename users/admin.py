from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "사용자 정보",
            {
                "fields": ("gender",
                 "role",
                 'profile_image',
                 "bio", "birthdate",
                 "current_status",
                 "attend"),
            },
        ),
        (
            "Health",
            {
                "fields": (            "height",
                 "weight",
                )
            },
        ),
        (
            "Wide Group",
            {
                "fields": (            "current_group",
                 "main_class",
                 "part_class")
            },
        ),
    )

    list_filter = UserAdmin.list_filter

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    filter_horizontal = UserAdmin.filter_horizontal + (
        "part_class",
    )
