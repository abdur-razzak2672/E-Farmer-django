from django.contrib import admin

from .models.seedModels import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(FartilizerProduct)
admin.site.register(PesticideProduct)
admin.site.register(AgriInstraction)

