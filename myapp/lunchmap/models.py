from cgitb import text
from cmath import atan
from unicodedata import name
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=255)
    #address = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline_at = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lunchmap:detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    category = models.ForeignKey(
        Shop,
        on_delete=models.PROTECT,
        null=True

    )
    txt = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.txt
