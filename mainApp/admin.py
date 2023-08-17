from django.contrib import admin
from .models import *

admin.site.register((Maincategory, Subcategory, Product, Brand,Buyer,Wishlist,Checkout,CheckoutProducts,Contact))
