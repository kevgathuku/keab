from django.contrib import admin


from .models import Crop, Farmer, Recommendation

admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(Recommendation)
