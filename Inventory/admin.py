from django.contrib import admin
from .models import Item, Client, Category, Transaction

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Transaction)