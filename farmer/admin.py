from django.contrib import admin


from .models import Buyer, Crop, Farmer, Order, Recommendation

admin.site.register(Buyer)
admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(Order)
admin.site.register(Recommendation)
