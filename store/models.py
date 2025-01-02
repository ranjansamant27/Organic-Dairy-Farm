from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Products(models.Model):
    CATEGORY_CHOICES=[
        (1,'dairy & poultry'),
        (2,'meat'),
        (3,'farm produce'),
        (4,'natural superfoods')
        
    ]
    name= models.CharField(max_length=100)
    price=models.IntegerField(default="10")
    details=models.CharField(max_length=500)
    image=models.ImageField(upload_to='images/images')
    is_active=models.BooleanField(default=True)
    category=models.IntegerField(choices=CATEGORY_CHOICES,default=1)
    
    def __str__(self):
        return self.name
    
    
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    
    
    def __str__(self):
        return str(
            (self.pid.name,
             self.uid.username)
            
        )
    

    
    
class Checkout(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name= models.CharField(max_length=100,default='name')
    address=models.TextField()
    phonenumber=models.IntegerField()
    pincode=models.IntegerField(default=0)
    date=models.DateField(default=datetime.datetime.today)
    
    
    def __str__(self):
        return str(self.name)
    
class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    amount=  models.FloatField(default=0)
    
    
    date=models.DateField(default=datetime.datetime.today)
    
    
    
    

    
    
    
    
    

    
    

    
    
    
    
    
