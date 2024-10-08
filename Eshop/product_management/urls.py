from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('productListing', views.productListing, name='productListing'),
    path('addToCart', views.addToCart, name='addToCart'),
    path('productDetail', views.productDetail, name='productDetail'),

    path('addProduct', views.addProduct, name='addProduct'),
    path('updateProduct', views.updateProduct, name='updateProduct'),
    path('removeProduct', views.removeProduct, name='removeProduct'),
    path('ManageAddProduct', views.ManageAddProduct, name='ManageAddProduct'),
    path('finalUpdateProduct', views.finalUpdateProduct, name='finalUpdateProduct'),
    path('updateProductToDB', views.updateProductToDB, name='updateProductToDB'),
    path('finalRemoveProduct', views.finalRemoveProduct, name='finalRemoveProduct'),
	path('checkout', views.checkout, name='checkout'),
]