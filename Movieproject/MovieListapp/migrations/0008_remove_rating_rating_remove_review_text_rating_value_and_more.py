# Generated by Django 4.2.6 on 2024-05-02 04:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListapp', '0007_alter_movie_trailer_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='text',
        ),
        migrations.AddField(
            model_name='rating',
            name='value',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(null=True, upload_to='poster'),
        ),
    ]
