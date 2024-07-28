from django.db import models

# Create your models here.
class PRODUCT(models.Model):

	#product details for database
	prodName = models.CharField(max_length = 100)
	prodPrice = models.FloatField()
	prodDesc = models.CharField(max_length = 100)
	prodAvailQuant = models.IntegerField()
	prodImage =  models.ImageField()
	prodCategory = models.CharField(max_length = 100)
