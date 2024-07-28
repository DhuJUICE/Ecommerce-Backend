from django.db import models
from product_management.models import PRODUCT
from django.contrib.auth.models import User, auth
# Create your models here.
class CART(models.Model):
	#user details for cart table in database - as foreign key to get values from User table
	userid = models.ForeignKey(User, on_delete=models.CASCADE)
	
	#product details for cart in database - - as foreign key to get values from PRODUCT table
	productid = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)

	#track the date and time the product was added to the cart
	datetimeAdded = models.DateTimeField()

	#track the quantity to buy of the specific product
	quantAdded = models.IntegerField()