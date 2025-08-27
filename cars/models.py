from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

class Cars(models.Model):
    car_name = models.CharField(max_length=20)
    car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='cars/media/upload')
    description = models.TextField(max_length=250)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def reduced_quantity(self):
        if self.quantity > 0:
            self.quantity -=1
            self.save()

    def __str__(self):
        return f'{self.car_name} - {self.car_brand} | price({self.price})'

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)

class Comments(models.Model):
    post = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    body = models.TextField(max_length=220)
    created_no = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return f'comments by {self.name}'