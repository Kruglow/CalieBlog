from autoslug.settings import slugify
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Logo(models.Model):
    logo = models.ImageField(upload_to='photo/logo/%Y/%m/%d', verbose_name='Лого')

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название поста')
    slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Автор')
    content = RichTextUploadingField(verbose_name='Контент',)
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    image = models.ImageField(upload_to='photo/post/%Y/%m/%d', verbose_name='Фото', blank=True,)
    category = models.ManyToManyField(Category, verbose_name='Категория', )
    tags = models.ManyToManyField('Tag', verbose_name='Теги')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


# class Author(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Имя')
#     photo = models.ImageField(upload_to='photo/author/%Y/%m/%d', verbose_name='Фото')
#     slug = models.SlugField(max_length=50, verbose_name='Слаг', unique=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('author', kwargs={'slug': self.slug})
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = 'Автор'
#         verbose_name_plural = 'Авторы'


class Comment(models.Model):
    email = models.EmailField()
    name = models.ForeignKey(User, on_delete=models.CASCADE,)
    website = models.CharField('Сайт', max_length=100)
    text = models.TextField('Сообщение', max_length=5000)
    date = models.DateTimeField('Дата',auto_now_add=True)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo/comments/%Y/%m/%d', verbose_name='Фото Пользователя', blank=True, default='default.png',)

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"


