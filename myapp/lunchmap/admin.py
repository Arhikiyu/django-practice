from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Category, Shop, Comment

admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Comment)
