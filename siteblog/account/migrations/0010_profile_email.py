# Generated by Django 4.0.6 on 2022-08-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile_facebook_profile_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='@2', max_length=254),
        ),
    ]
