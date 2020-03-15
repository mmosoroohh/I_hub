from django.db import models
from rest_framework.response import Response


# Create your models here.
class Process(models.Model):
    process_name = models.CharField(max_length=255, null=False)
    owner = models.CharField(max_length=255, null=False)

    # owner = models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE)

    def __str__(self):
        return self.process_name


class Assets(models.Model):
    asset_name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    process = models.ForeignKey(Process, related_name='Asset_process', on_delete=models.CASCADE)
    duration = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.asset_name


class Groups(models.Model):
    group_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.group_name


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


class Report(models.Model):
    report_name = models.CharField(max_length=255, null=False)
    record = models.ForeignKey(Process, related_name='Report_record', on_delete=models.CASCADE)
    maps = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.report_name


class DataInputs(models.Model):
    data_subjects = models.CharField(max_length=255, null=False)
    data_items = models.CharField(max_length=255, null=False)
    data_sources = models.CharField(max_length=255, null=False)


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.username
