from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models.seedModels import * 
from .utils import cookieCart, cartData, guestOrder
from django.db.models import Q

def search(request):
    	
	if request.method=="POST":
		data = cartData(request)
		cartItems = data['cartItems']
	 
		searched =request.POST['searched']
		products = Product.objects.filter(name__contains =searched)
		context = {'searched':searched, 'productItems':products, 'cartItems':cartItems}
		return render(request , 'farmer/store/search.html', context)
	else:
		g

    		

def homepage(request):
	data = cartData(request)
	cartItems = data['cartItems']
	context = {'cartItems':cartItems}
	return render(request, 'farmer/homepage.html', context)


def fartilizer(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = FartilizerProduct.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'farmer/store/fartilizer.html',context)



def pesticide(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	products = PesticideProduct.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'farmer/store/pesticide.html',context)




def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'farmer/store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'farmer/store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'farmer/store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

# Agri instractions


def instraction(request):
    	
	data = cartData(request)
	cartItems = data['cartItems']
	instractions = AgriInstraction.objects.all()
	context = {'instractions':instractions ,'cartItems':cartItems}
	return render(request, 'farmer/agri_instractions/instractions.html', context)


def solution(request):
    	    	
	data = cartData(request)
	cartItems = data['cartItems']
	solutions = AgriSolution.objects.all()
	context = {'solutions':solutions,'cartItems':cartItems}
	return render(request, 'farmer/solution.html', context)

def loan(request):
    	    	
	data = cartData(request)
	cartItems = data['cartItems']
	context = {'cartItems':cartItems}
	return render(request, 'farmer/loan.html', context)


def profile(request):
    	    	
	data = cartData(request)
	cartItems = data['cartItems']
	context = {'cartItems':cartItems}
	return render(request, 'farmer/profile.html', context)


def about(request):
    	    	
	data = cartData(request)
	cartItems = data['cartItems']
	context = {'cartItems':cartItems}
	return render(request, 'farmer/about.html', context)