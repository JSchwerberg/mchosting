from django.db import models
from django.contrib.auth.models import User

# Abstract Classes 

class Feature(models.Model):
    name = models.CharField(max_length=60)
    internal_name = models.CharField(max_length=20)
    short_desc = models.CharField(max_length=160)
    desc = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']

class Plan(models.Model):
    name = models.CharField(max_length=60)
    short_desc = models.CharField(max_length=160)
    desc = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    active = models.BooleanField()

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']

class Service(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField()

    class Meta:
        abstract = True
        ordering = ['id']

# Inherited Models

# Example
#
# class ExampleFeature(Feature):
#     ....
# 
# class ExamplePlan(Plan):
#     ....
#     included_features = models.ManyToManyField(ExampleFeatures)
#
# class ExampleService(Service):
#     plan = models.ForeignKey(ExamplePlan)
#     features = models.ManyToManyField(ExampleFeatures)

class MinecraftFeature(Feature):
    required_memory = models.BigIntegerField()
    required_storage = models.BigIntegerField()

class MinecraftPlan(Plan):
    max_memory = models.BigIntegerField()
    max_storage = models.BigIntegerField()
    included_features = models.ManyToManyField(MinecraftFeature)

class MinecraftService(Service):
    plan = models.ForeignKey(MinecraftPlan)
    features = models.ManyToManyField(MinecraftFeature)

    def __unicode__(self):
        return str(self.id)
