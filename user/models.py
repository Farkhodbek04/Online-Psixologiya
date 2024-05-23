from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from functools import reduce


class CoreModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    icon = models.ImageField(upload_to='avatar/', blank=True, null=True)
    status = models.CharField(max_length=10)
    tel_number = models.CharField(max_length=13)

class Category(CoreModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Blog(CoreModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    blog_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blogs')

    @property
    def review(self):
        reviews = BlogReview.objects.filter(blog=self)
        result = reduce(lambda result, x: result + x.mark, reviews, 0)
        try:
            result = round(result / reviews.count())
        except ZeroDivisionError:
            result = 0
        return result

    @property
    def is_active(self):
        return self.quantity > 0

    def __str__(self):
        return self.title

    @property
    def is_discount(self):
        if self.discount_price is None:
            return 0
        return self.discount_price > 0

class BlogImage(CoreModel):
    image = models.ImageField(upload_to='blog_images/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')

class BlogReview(CoreModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='reviews')
    mark = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        object = BlogReview.objects.filter(user=self.user, blog=self.blog)
        if object.count():
            object.delete()
            super(BlogReview, self).save(*args, **kwargs)
        else:
            super(BlogReview, self).save(*args, **kwargs)

class Service(CoreModel):
    psycholog = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    baner_image = models.ImageField(upload_to='services_baner/')

class ContactUs(CoreModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
