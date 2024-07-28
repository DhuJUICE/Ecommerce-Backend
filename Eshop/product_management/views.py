from django.shortcuts import render, redirect, get_object_or_404
from .models import PRODUCT
from cart_management.models import CART
from django.contrib.auth.models import User, auth
import datetime

# Create your views here.
def productListing(request):
	products = PRODUCT.objects.all()
	return render(request, 'product_listing.html', {'products': products})

#function to display the details about a specificly selected product from product_listing
def productDetail(request):
	productid = request.POST['productNum']
	displayProd = PRODUCT.objects.get(id=productid)
	return render(request, 'product_detail.html', {'displayProduct' : displayProd})

#create function to add items to shopping cart
def addToCart(request):
	productid = request.POST['productid']
	userid = request.POST['userid']
	quantAdded = request.POST['prodQuantity']

	#check to see if the quantity is valid or no
	if quantAdded == "" or quantAdded == 0:
		print("Quantity incorrect or 0")
	else:
		print("Adding to cart")

		#check to see if there is already a product in the cart with th userid and productid of the new product the user wants to add to their cart
		user = User.objects.get(pk=userid)
		product = PRODUCT.objects.get(pk=productid)

		#check to see if this cart object already exists with the user and product objects
		try:
			CART.objects.get(userid=user, productid=product)
			print("object does exist - can i just add your new order quantity to the existing cart product order quantity")
		except CART.DoesNotExist:
			#create a cart object to add the selected product to the user's cart
			cart = CART.objects.create(userid=user, productid=product, datetimeAdded=datetime.datetime.now(), quantAdded=quantAdded)
		
			#save the new user data to the database
			cart.save();

	#redirect me to the product listing/browsing page
	return redirect("productListing")


#function to add products to the database
def addProduct(request):
	return render(request, 'addProducts.html')

#function to add products to the database
def updateProduct(request):
	products = PRODUCT.objects.all()
	response = {'products' : products}
	return render(request, 'updateProducts.html', response)

#function to add products to the database
def removeProduct(request):
	products = PRODUCT.objects.all()
	response = {'products' : products}
	return render(request, 'removeProducts.html', response)

#function to add products to database from manage products - add products page
def ManageAddProduct(request):
	#get product details from add page
	prodName = request.POST['prodName']
	prodPrice = request.POST['prodPrice']
	prodDesc = request.POST['prodDesc']
	prodAvailQuant = request.POST['prodQuantity']
	prodImage = request.POST['prodImage']
	prodCategory = request.POST['prodCategory']

	#create product object to send to database
	product = PRODUCT.objects.create(prodName=prodName, prodPrice=prodPrice, prodDesc=prodDesc, prodAvailQuant=prodAvailQuant, prodImage=prodImage, prodCategory=prodCategory)

	#refresh the add page
	return redirect ('addProduct')

#function to send superuser selected products to be updated to update page
def finalUpdateProduct(request):
	productId = request.POST['productNum']
	print(productId)
	product = PRODUCT.objects.get(id=productId)

	response = {'product' : product}
	return render(request, 'finalUpdateProducts.html', response)

#function to delete product form database
def finalRemoveProduct(request):
	productId = request.POST['productNum']

	product = PRODUCT.objects.get(id=productId)

	#delete the product from database
	product.delete()

	#get the remaining objects
	products = PRODUCT.objects.all()
	response = {'products' : products}

	return render(request, 'removeProducts.html', response)

#fundtion to update the product into database
def updateProductToDB(request):
	#get product details from add page
	prodName = request.POST['prodName']
	prodPrice = request.POST['prodPrice']
	prodDesc = request.POST['prodDesc']
	prodAvailQuant = request.POST['prodQuantity']
	prodImage = request.POST['prodImage']
	prodCategory = request.POST['prodCategory']

	productid = request.POST['productid']
	product = PRODUCT.objects.get(id=productid)

	if prodName != "":
		product.prodName = prodName

	if prodPrice != "":
		product.prodPrice = prodPrice

	if prodDesc != "":
		product.prodDesc = prodDesc

	if prodAvailQuant != "":
		product.prodAvailQuant = prodAvailQuant

	if prodImage != "":
		product.prodImage = prodImage

	if prodCategory != "":
		product.prodCategory = prodCategory
		


	product.save()

	response = {'product' : product}
	return render(request, 'finalUpdateProducts.html', response)