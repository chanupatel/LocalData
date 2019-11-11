from django.db import models


# Create your models here.
class TitleDetails(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    offers = models.BooleanField(default=False)


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()
    price = models.IntegerField()
    timestamp = models.TimeField()


class Users(models.Model):
    fName = models.CharField(max_length=100)
    lName = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    dob = models.DateTimeField()
    sex = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    timestamp = models.TimeField()
    regTime = models.DateTimeField()

