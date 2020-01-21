from django.db import models
from django.core.validators import RegexValidator


# Create your models here.


class details(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200, default='not entered')
    gender = models.CharField(max_length=200)
    door_no = models.CharField(max_length=200, default='not provided')
    age = models.CharField(max_length=200)
    voter_id = models.CharField(max_length=200, default='not provided')


class women(models.Model):
    name = models.CharField(max_length=200)
    husband_name = models.CharField(max_length=200, default='not entered')
    gender = models.CharField(max_length=200)
    door_no = models.CharField(max_length=200, default='not provided')
    age = models.CharField(max_length=200)
    voter_id = models.CharField(max_length=200, default='not provided')
