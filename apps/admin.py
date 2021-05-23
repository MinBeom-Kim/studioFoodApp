from django.contrib import admin
from . import models

@admin.register(
    models.Group,
    models.Class,
)
class AppsAdmin(admin.ModelAdmin):

    """ Apps Admin Definition """
