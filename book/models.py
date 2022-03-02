"""
Function based Views
Model name : Book  
database table name : book
Custom manager : ActiveBookManager
------------------------------------------------------
Class based Views
Model name : Employee  
database table name : emp
"""

from django.db import models

print("In models.py")
# Create your models here.

class ActiveBookManager(models.Manager):                                                # custom model manager to get all is_active books
    def get_queryset(self):
        return super(ActiveBookManager, self).get_queryset().filter(is_active=True)

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_obj = ActiveBookManager()                                                    # custom model manager object
    
    class Meta:
        db_table = "book"
    
    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()

    class Meta:
        db_table = "emp"
    
    def __str__(self):
        return f"{self.first_name}"

