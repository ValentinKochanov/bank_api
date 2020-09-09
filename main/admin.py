from django.contrib import admin
from .models import Account, Customer, Replenishment, Outlay, Master_Account


admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Replenishment)
admin.site.register(Outlay)
admin.site.register(Master_Account)
