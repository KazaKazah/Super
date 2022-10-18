from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts', verbose_name='автор')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Пост'
        verbose_name_plural='Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": str(self.slug)})


class PostBody(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    body = models.TextField(verbose_name='описание')
    post = models.ForeignKey(
        Post,
        on_delete=models.PROTECT,
        related_name='body_list'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительные данные'
        verbose_name_plural='Дополнительные данные'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    name = models.CharField(max_length=80, verbose_name='название')
    email = models.EmailField(verbose_name='адресс электронной почты')
    body = models.TextField(verbose_name='коментарии')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Комментарии'
        verbose_name_plural='Комментарии'


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
