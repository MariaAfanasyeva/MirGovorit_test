# Generated by Django 5.0.1 on 2024-01-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeproduct',
            name='weight',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
