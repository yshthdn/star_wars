# Generated by Django 3.2 on 2021-04-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planet_movies', '0002_auto_20210413_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='movie',
            new_name='films',
        ),
        migrations.RenameField(
            model_name='planet',
            old_name='planet_name',
            new_name='name',
        ),
    ]