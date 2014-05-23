from django.db import models


class DepartmentManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def natural_key(self):
        return self.name

    def __unicode__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

