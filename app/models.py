from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import re
# Create your models here.

class Balance_inq(models.Model):
    '''For Balance Inquiry'''
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

class TransactionHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    dateTime_field = models.DateTimeField(default = datetime.now, blank = True)
    remaining_amount = models.IntegerField()
    withdrawl_amount = models.IntegerField()

    