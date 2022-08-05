from autoslug.settings import slugify
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=500,verbose_name='О себе',blank=True)
    inst = models.URLField(default='ins', blank=True)
    facebook = models.URLField(default='facebook', blank=True)
    twitter = models.URLField(default='twitter', blank=True)
    slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True, default='Users')
    email = models.EmailField(default='@2')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        return super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('user', kwargs={'slug': self.slug})
