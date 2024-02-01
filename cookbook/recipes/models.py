from django.db import models


class RecipeManager(models.Manager):
    def recipes_with_product(self, product):
        return self.get_queryset().filter(products=product, recipeproduct__weight__gte=10)

    def recipes_without_product(self, product):
        return self.get_queryset().difference(self.recipes_with_product(product))


class Product(models.Model):
    name = models.CharField(max_length=50)
    usage_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(
        Product,
        through="RecipeProduct",
        through_fields=("recipe", "product"),
    )
    objects = RecipeManager()

    def __str__(self):
        return self.name

    def add_product(self, product, weight):
        recipe_product, created = RecipeProduct.objects.get_or_create(
            recipe=self,
            product=product,
            defaults={"weight": weight},
        )

        if not created:
            recipe_product.weight = weight
            recipe_product.save()

    def cook(self):
        for product in self.products.all():
            product.usage_count += 1
            product.save()


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return f"{self.product} in {self.recipe}"
