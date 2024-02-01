from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


admin.site.register(Product)
# admin.site.register(Recipe)
admin.site.register(RecipeProduct)


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]

