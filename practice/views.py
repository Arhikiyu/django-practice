from django.shortcuts import render
from django.http import HttpResponse
from .models import comment


def index(request):
    context = {
        'message': 'Welcome my Django',
        'players': ["Aさん", "Bさん", "Cさん"],
        'comments': comment.objects.all()
    }
    return render(request, 'practice/index.html', context)
