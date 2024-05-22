from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from functools import reduce


class CustomUser(AbstractUser):
    f_name = models.CharField(max_length=30, default='deafault')
    l_name = models.CharField(max_length=30, default='default')
    icon = models.ImageField(upload_to='avatar/', blank=True, null=True)
    status = models.CharField(max_length=10)
    tel_number = models.CharField(max_length=13)
    

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    @property
    def review(self):
        reviews = BlogReview.objects.filter(Blog_id=self.id)
        result = reduce(lambda result, x: result +x.mark, reviews, 0)
        try: 
            result = round(result / reviews.count())

        except  ZeroDivisionError:
            result=0
        return result
    
    @property 
    def is_active(self):
        return self.quantity > 0
    
    def __str__(self) -> str:
        return self.name
    
    @property 
    def is_discount(self):
        if self.discount_price is None:
            return 0
        return self.discount_price > 0


class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class BlogReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    mark = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        object = BlogReview.objects.filter(user=self.user, 
        Blog=self.Blog)
        if object.count():
            object.delete()
            super(BlogReview, self).save(*args, **kwargs)
        else:
            super(BlogReview, self).save(*args, **kwargs)


class ContactUs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
