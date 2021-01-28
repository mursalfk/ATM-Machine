from django.db import models


# class DataClass(models.Model):
#     '''Attribute => Name of the Variable = model.Type of the Field (further constrainsta)'''
#     # user_id = models.IntegerField()
#     # username = models.TextField(max_length=200, default="username")
#     name = models.CharField(max_length=200)
#     # pin = models.IntegerField(default="1111")
#     # account_status = models.TextField(max_length=200, default="inactive")
#     password = models.CharField(max_length=200, default="password")
#     # balance = models.IntegerField(default="0")

# #     def __str__(self):
# #         return self.name

# class Transaction(models.Model):
#     '''Replace these names with ID when you learn them completely'''
#     user_id = models.ForeignKey(DataClass, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     time = models.TimeField(auto_now_add=True)
#     action = models.CharField(max_length=200, default="username")

# class Transaction_dummy(models.Model):
#     '''Replace these names with ID when you learn them completely'''
#     user_id = models.ForeignKey(DataClass, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
#     time = models.TimeField(auto_now_add=True)
#     action = models.CharField(max_length=200, default="username")
# #     def __str__(self):
# #         return self.text

