# Generated by Django 4.2.6 on 2024-04-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='movie_posters/'),
        ),
    ]