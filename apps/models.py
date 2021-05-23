from django.db import models
# from users import models as users_models

class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Group(models.Model):
  name = models.CharField(max_length=200)
  profile_image = models.ImageField(null=True, default="", blank=True)
  bio = models.TextField(default="", blank=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

class Class(models.Model):
  """ Class """
  name = models.CharField(max_length=200, unique=True)
  group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
  profile_image = models.ImageField(upload_to="group/image", null=True, default="", blank=True)
  bio = models.TextField(default="", blank=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name

  
  @property
  def user_count(self):
    return self.users.all().count()
    
  @property
  def user_name(self):
    return self.users.all()