# Generated by Django 4.2.6 on 2024-04-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListapp', '0005_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer_link',
            field=models.URLField(max_length=255),
        ),
    ]