from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Product, Recipe, RecipeProduct


def add_product_to_recipe(request):
    recipe_id = request.GET.get("recipe_id")
    product_id = request.GET.get("product_id")
    weight = request.GET.get("weight")

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)

    recipe.add_product(product=product, weight=weight)

    return HttpResponse(status=200)


def cook_recipe(request):
    recipe_id = request.GET.get("recipe_id")
    recipe = get_object_or_404(Recipe, id=recipe_id)

    recipe.cook()

    return HttpResponse(status=200)


def show_recipes_without_product(request):
    product_id = request.GET.get("product_id")
    product = get_object_or_404(Product, id=product_id)

    recipes_without_product = Recipe.objects.recipes_without_product(product)

    '''
    recipes_without_product = dict()
    recipes = Recipe.objects.all()
    for idx, recipe in enumerate(recipes, start=1):
        if (product not in recipe.products.all() or
                RecipeProduct.objects.get(product=product, recipe=recipe).weight < 10):
            recipes_without_product[idx] = recipe
    '''

    context = {'recipes_without_product': recipes_without_product}
    return render(request, 'recipes/show_recipes_without_product.html', context)
