from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.

def index(request):
    return HttpResponse('Hello, World')


def showRay(request):
    return render(request, 'index.html')


def showArticle(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'index.html', {'article': article})
