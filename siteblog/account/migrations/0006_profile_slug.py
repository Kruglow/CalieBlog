# Generated by Django 4.0.6 on 2022-07-31 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='Users', unique=True, verbose_name='Слаг'),
        ),
    ]
