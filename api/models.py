from django.db import models
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class Process(models.Model):
    process_name = models.CharField(max_length=255, null=False)
    owner = models.CharField(max_length=255, null=False)
    acting_as = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.process_name


class Groups(models.Model):
    group_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.group_name


class Assets(models.Model):
    asset_name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    processor = models.CharField(max_length=255, null=False)
    operator = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.asset_name


class DataClassification(models.Model):
    data_name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.data_name


class DataMaps(models.Model):
    image = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class DataSubject(models.Model):
    name = models.CharField(max_length=255, null=False)


class DataItems(models.Model):
    name = models.CharField(max_length=255, null=False)


class SubjectSource(models.Model):
    name = models.CharField(max_length=255, null=False)
    subject = models.ForeignKey(DataSubject, on_delete=models.CASCADE)
    source = models.ForeignKey(Assets, on_delete=models.CASCADE)


class UsersManager(BaseUserManager):
    """Users model manager"""

    def create_user(self, username, password=None, is_active=True, is_admin=False):
        user = self.model(username=username)
        user.active = is_active
        user.admin = is_admin
        user.set_password(password)
        user.save()
        return user

    def create_normaluser(self, username):
        """Create regular user."""
        return self.create_user(username)


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)

    objects = UsersManager()

    def __str__(self):
        return self.username
