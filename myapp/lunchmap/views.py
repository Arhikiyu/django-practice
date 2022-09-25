from pyexpat import model
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.views import generic
from pyrsistent import field
from .models import Category, Shop, Comment
from django.urls import reverse_lazy


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


class DeleteView(generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('lunchmap:index')


class CommentCreate(generic.CreateView):
    """コメント投稿ページのビュー"""
    template_name = 'comment_form.html'
    model = Comment
    #form_class = CommentCreateForm
