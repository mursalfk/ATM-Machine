from django.contrib import admin
from .models import Balance_inq, TransactionHistory

# Register your models here.

admin.site.register(Balance_inq)
admin.site.register(TransactionHistory)