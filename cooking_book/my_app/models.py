from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="category_name")
    number_of_uses = models.IntegerField(null=True, verbose_name="number_of_uses", default=0)
    
    def __str__(self):
        return f"{self.name}"
    
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    def __str__(self):
        return self.name

class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField(null=True, default=0)

    class Meta:
        unique_together = ('recipe', 'product')