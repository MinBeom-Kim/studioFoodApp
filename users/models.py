from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    ROLE_TEACHER = "teacher"
    ROLE_CHILD = "child"
    ROLE_PARENT = "parent"

    ROLE_CHOICES = (
        (ROLE_TEACHER, "선생님"),
        (ROLE_CHILD, "어린이"),
        (ROLE_PARENT, " 부모"),
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)
    profile_image = models.ImageField(null=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True, blank=True)
