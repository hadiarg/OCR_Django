from django.contrib import admin

from web.models import Customer
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Ocr_Note)