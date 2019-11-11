from django.contrib import admin
from .models import Destination, Users, TitleDetails

# Register your models here.
admin.site.register(Destination)
admin.site.register(Users)
admin.site.register(TitleDetails)