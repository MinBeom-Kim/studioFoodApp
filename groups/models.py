from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    profile_image = models.ImageField(null=True, default="", blank=True)
    bio = models.TextField(default="", blank=True)