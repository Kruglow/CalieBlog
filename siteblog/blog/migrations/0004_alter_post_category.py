# Generated by Django 4.0.6 on 2022-07-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='blog.category', verbose_name='Категория'),
        ),
    ]