from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(
        max_length=100
    )


    def __str__(self):
        return self.name



class Book(models.Model):

    title = models.CharField(
        max_length=200
    )

    author = models.CharField(
        max_length=200
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    isbn = models.CharField(
        max_length=20,
        unique=True
    )

    cover = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True
    )

    available = models.BooleanField(
        default=True
    )

    borrower = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title