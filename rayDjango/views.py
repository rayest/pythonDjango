# coding=utf-8
import json

import json as simplejson

from django.http import HttpResponse, JsonResponse
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
    params = json.loads(request.body)
    title = params.get('title')
    content = params.get('content')
    title = request.POST.get('title', title)
    content = request.POST.get('content', content)
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


@csrf_exempt
def getJson(request):
    params = json.loads(request.body)
    title = params.get('title')
    content = params.get('content')
    data = {
        "title": title,
        "content": content
    }
    return HttpResponse(simplejson.dumps(data))
