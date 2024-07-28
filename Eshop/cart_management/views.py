from django.shortcuts import render, redirect
from .models import CART
from product_management.models import PRODUCT
from django.contrib.auth.models import User, auth
# Create your views here.
#create function to open the cart page and to display all items in the specific user''s cart
def openCart(request):
	userid = request.POST['useridCart']

	#get all the CART recodrs from the database tables
	cartProducts = CART.objects.filter(userid=userid)

	totalPurchaseTotal = 0
	for item in cartProducts:
		item.product_total = item.quantAdded * item.productid.prodPrice
		totalPurchaseTotal += item.product_total

	response = {'displayProducts' : cartProducts, 'totalPurchaseTotal' : totalPurchaseTotal}

	return render(request, 'cart.html', response)

#function to delete cart objects from database if they are removed by the user
def removeFromCart(request):
	#need to get userid and productid from the cart product to remove
	cartid = request.POST['cartid']
	userid = request.POST['userid']
	productid = request.POST['productNum']

	#get the object you want to delete from the cart
	deleteCartProduct = CART.objects.get(id=cartid)

	#delete the object after it is retrieved from database
	deleteCartProduct.delete()

	#get all the objects/records from the database tables for the specific logged in user
	cartProducts = CART.objects.filter(userid=userid)

	totalPurchaseTotal = 0
	for item in cartProducts:
		item.product_total = item.quantAdded * item.productid.prodPrice
		totalPurchaseTotal += item.product_total

	response = {'displayProducts' : cartProducts, 'totalPurchaseTotal' : totalPurchaseTotal}

	return render(request, 'cart.html', response)