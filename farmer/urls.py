from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name = "homepage"),
    path('store/',views.store, name = "store"),
    path('fartilizer/',views.fartilizer, name = "fartilizer"),
    path('pesticide/',views.pesticide, name = "pesticide"),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('instractions/', views.instraction, name="instractions"),

]