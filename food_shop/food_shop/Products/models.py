from django.db import models

class Product(models.Model):
      title = models.CharField(max_length=200)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      description = models.TextField()
      stock = models.IntegerField()
      price_1kg = models.DecimalField(max_digits=10,decimal_places=2)
      image = models.ImageField(upload_to='images/', default='default.jpg')

      def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

