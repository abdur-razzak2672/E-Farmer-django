from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name = "homepage"),
    path('store/',views.store, name = "store"),
    path('search/',views.search, name = "search"),
    path('fartilizer/',views.fartilizer, name = "fartilizer"),
    path('pesticide/',views.pesticide, name = "pesticide"),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('instractions/', views.instraction, name="instractions"),
    path('loan/', views.loan, name="loan"),
    path('solutions/', views.solution, name="solution"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addProduct/',views.addProduct, name = "addProduct"),


]