# Generated by Django 4.2.6 on 2024-04-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListapp', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
