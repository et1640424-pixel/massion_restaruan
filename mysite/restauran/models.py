from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    frist_name = models.CharField(max_length=20)


class Category(models.Model):
    title = models.CharField(max_length=20)


class Restaurant(models.Model):
    name = models.CharField(max_length=20)

class menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Product(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class book(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def get_total_price(self):
        return sum([i.get_total_price() for i in self.item.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price

class Favorite(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='favorite_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


