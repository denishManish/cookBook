# Generated by Django 5.0.1 on 2024-01-27 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_product_usage_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='product',
            new_name='products',
        ),
    ]