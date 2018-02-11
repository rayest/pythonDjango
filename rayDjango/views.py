# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models


# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse('Hello, World')


def showRay(request):
    return render(request, 'index.html')


def showArticle(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'index.html', {'article': article})


@csrf_exempt
def create(request):
    title = request.POST.get('title', "这是标题")
    content = request.POST.get('content', "这是内容")
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
