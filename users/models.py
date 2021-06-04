from django.contrib.auth.models import AbstractUser
from django.db import models
from apps import models as apps_models

class AbstractItem(apps_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PartClass(AbstractItem):

    """ PartClass Model Definition """

    class Meta:
        verbose_name_plural = "PartClasss"
        ordering = ["name"]


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

    STATUS = [
      ('active', '활성화'),
      ('inactive', '비활성화')
    ]

    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10)
    profile_image = models.ImageField(upload_to="user/image", null=True, default="", blank=True)
    bio = models.TextField(default="", blank=True)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    birthdate = models.DateField(null=True, blank=True)
    attend = models.IntegerField(default=0)
    current_status        = models.CharField(max_length=10, choices=STATUS, default='active')
    current_group         = models.ForeignKey(apps_models.Group, on_delete=models.SET_NULL, blank=True, null=True)
    
    main_class = models.ForeignKey(apps_models.Class, on_delete=models.SET_NULL, blank=True, null=True)

    part_class = models.ManyToManyField(apps_models.Class, related_name="users", blank=True)

    @property
    def class_count(self):
        return self.part_class.all().count()
    
    @property
    def class_name(self):
        return self.part_class.all()
    
    @property
    def attend_count(self):
        return 0



