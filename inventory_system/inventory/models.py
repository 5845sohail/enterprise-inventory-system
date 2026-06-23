from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, #cascade used for if category is delete then its product will also be delete
        related_name='products'  
        )
    name = models.CharField(max_length=100) 
    quantity = models.IntegerField(default=0) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    date_added= models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contant_email = models.EmailField()
    date_joined= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name