from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=400)
    def __unicode__(self):
        return self.name
class Adhaar(models.Model):
    uid=models.BigIntegerField(unique=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=3)
    yob=models.IntegerField()
    dep=models.CharField(max_length=100)
    lm=models.CharField(max_length=20)
    loc=models.CharField(max_length=100)
    vtc=models.CharField(max_length=100)
    po=models.CharField(max_length=100)
    dist=models.CharField(max_length=100)
    state=models.CharField(max_length=20)
    pc=models.IntegerField()
    mobile=models.BigIntegerField()
    
    def __unicode__(self):
        return self.name
class Login(models.Model):
    uid=models.BigIntegerField()
    pc=models.IntegerField()
    def __unicode__(self):
        return self.name
    
class LoggedIn(models.Model):
    userid=models.BigIntegerField()
