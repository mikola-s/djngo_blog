from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    create_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_username()


class Article(models.Model):
    pass


class Comments(models.Model):
    pass


class Expression(models.Model):
    pass


class ExpressionType(models.Model):
    pass
