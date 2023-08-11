from django.db import models
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=200,blank=True)
    date_added=models.DateField(auto_now_add=True)


    class Meta:
        db_table="Cart"
        ordering=["date_added"]

    def __str__(self):
        return '{}'.format(self.cart_id)
    

#for storing added items in the cart

class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table="CartItem"

    # for getting total amount of items with their qunatity,this function is used

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)        