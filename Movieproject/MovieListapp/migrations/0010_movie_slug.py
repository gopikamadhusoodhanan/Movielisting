# Generated by Django 4.2.6 on 2024-05-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieListapp', '0009_rating_created_at_alter_rating_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
