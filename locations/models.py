from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.utils import timezone
from django.conf import settings



class User(AbstractUser):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=30,choices=GENDER, null=True)
    age=models.IntegerField(null=True)


class Location(models.Model):
	poster=models.CharField(max_length=40)
	country = models.CharField(max_length=60)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	city = models.CharField(max_length=30, null=True, blank=True)
	reported_time = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='properties/')
	description = models.TextField(default='devastation')
	district = models.CharField(max_length=30)
	sector = models.CharField(max_length=30)
	cell = models.CharField(max_length=30)
	village = models.CharField(max_length=30)

	def __str__(self):
		return self.city

class Contact(models.Model):
	name=models.CharField(max_length=100,null=True,blank=True)
	email=models.EmailField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField(max_length=3000)
	created_at=models.DateTimeField(auto_now=True)


	