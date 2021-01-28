from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Balance_inq(models.Model):
    '''For Balance Inquiry'''
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.CharField(max_length = 20, default = None)

class TransactionHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    dateTime_field = models.DateTimeField(default = datetime.now, blank = True)
    remaining_amount = models.CharField(max_length = 20, default = None)
    withdrawl_amount = models.CharField(max_length = 20, default = None)

    
