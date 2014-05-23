from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)


class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    department = models.ForeignKey(Department)

