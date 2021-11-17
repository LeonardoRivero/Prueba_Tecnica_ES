from django.contrib import admin
from .models import Camera, FilmCamera, TechnicalSupport, ItemsCamera, Leasing, Client, ModelCamera

# Register your models here.
admin.site.register(Camera)
admin.site.register(FilmCamera)
admin.site.register(TechnicalSupport)
admin.site.register(ItemsCamera)
admin.site.register(Leasing)
admin.site.register(Client)
admin.site.register(ModelCamera)
