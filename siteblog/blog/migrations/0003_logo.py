# Generated by Django 4.0.6 on 2022-07-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_author_post_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='photo/logo/%Y/%m/%d', verbose_name='Лого')),
            ],
        ),
    ]
