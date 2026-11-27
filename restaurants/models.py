from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Restaurant
class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    address=models.TextField()
    contact_number=models.CharField(max_length=12)
    email=models.EmailField()
    image=models.ImageField(upload_to='image',blank=True,null=True)
    opening_time=models.TimeField()
    closing_time=models.TimeField()
    is_active=models.BooleanField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

#MenuItem
class MenuItem(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    menu_name=models.CharField(max_length=100)
    menu_descripion=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    menu_image=models.ImageField(upload_to='menu_image')
    category=models.CharField(max_length=100)
    is_available=models.BooleanField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menu_name

#RestaurantLike
class RestaurantLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

# MenuItemLike
class MenuItemLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)

# MenuItemSave
class MenuItemSave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)



