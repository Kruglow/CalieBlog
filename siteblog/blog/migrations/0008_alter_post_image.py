# Generated by Django 4.0.6 on 2022-07-26 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/post/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]