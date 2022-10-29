from django.db import models

class Location(models.Model):
	country = models.CharField(max_length=60)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)

	def __str__(self):
		return self.country
