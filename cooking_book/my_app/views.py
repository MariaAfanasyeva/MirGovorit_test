# views.py

from django.db import transaction
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct

@transaction.atomic
def add_product_to_recipe(request, recipe_id, product_id, weight):
    try:
        if request.method == 'GET':
            recipe = Recipe.objects.get(pk=recipe_id)
            product = Product.objects.get(pk=product_id)

            recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
            recipe_product.weight = weight
            recipe_product.save()
            
            return HttpResponse("Product added to recipe successfully.")

    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)

@transaction.atomic
def cook_recipe(request, recipe_id):
    try:
        if request.method == 'GET':
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe_products = RecipeProduct.objects.prefetch_related("product").filter(recipe=recipe)

            for recipe_product in recipe_products:
                recipe_product.product.number_of_uses += 1
                recipe_product.product.save()
                
            return HttpResponse("Recipe cooked successfully.")
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)

@transaction.atomic
def show_recipes_without_product(request, product_id):
    try:
        if request.method == 'GET':
            recipes = Recipe.objects.filter(~Q(recipeproduct__product_id=product_id) | (Q(recipeproduct__product_id=product_id) & Q(recipeproduct__weight__lte=10))).distinct()
            return render(request, 'recipes_without_product.html', {'recipes': recipes})
    except Exception as e:
        return HttpResponse("An error occurred: {}".format(str(e)), status=500)
