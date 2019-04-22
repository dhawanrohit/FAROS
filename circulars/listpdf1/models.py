from django.db import models

# Create your models here.
class Circulars(models.Model):
	circular_id = models.CharField(max_length=200)


	def __str__(self):
		return self.circular_id