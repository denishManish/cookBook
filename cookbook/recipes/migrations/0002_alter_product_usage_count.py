# Generated by Django 5.0.1 on 2024-01-26 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='usage_count',
            field=models.IntegerField(default=0),
        ),
    ]
