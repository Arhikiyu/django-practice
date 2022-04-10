from django.shortcuts import render
from django.views import generic
from pyrsistent import field
from .models import Category, Shop


class IndexView(generic.ListView):
    model = Shop


class DetailView(generic.DetailView):
    model = Shop


class CreateView(generic.edit.CreateView):
    model = Shop
    fields = '__all__'


class UpdateView(generic.edit.UpdateView):
    model = Shop
    fields = '__all__'
