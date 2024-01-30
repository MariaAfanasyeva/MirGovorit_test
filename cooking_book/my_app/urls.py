from django.urls import path
from . import views

urlpatterns = [
    path('add_product_to_recipe/<recipe_id>/<product_id>/<weight>', views.add_product_to_recipe, name='add_product_to_recipe'),
    path('cook_recipe/<recipe_id>', views.cook_recipe, name='cook_recipe'),
    path('show_recipes_without_product/<product_id>', views.show_recipes_without_product, name='show_recipes_without_product'),
]

