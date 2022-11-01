from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class OurTeam(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	job_title = models.CharField(max_length=30)
	photo = models.ImageField()
	member_descriptions = models.TextField()

	def __str__(self):
		return self.name

class Location(models.Model):
	country = models.CharField(max_length=60)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	city = models.CharField(max_length=30, null=True, blank=True)
	street = models.CharField(max_length=20, null=True, blank=True)
	reported_time = models.DateTimeField(default=timezone.now)
	image = models.ImageField(upload_to='properties/')
	description = models.TextField(default='devastation')


	def __str__(self):
		return self.country

class TeamSocialMedia(models.Model):
	user = models.ForeignKey(OurTeam, on_delete=models.CASCADE)
	twitter = models.URLField()
	facebook = models.URLField()
	instgram = models.URLField()
	linkedin = models.URLField()

	def __str__(self):
		return self.user
