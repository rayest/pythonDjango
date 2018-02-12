from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^lee$', views.index),
    url('^ray$', views.showRay),
    url('^article/id/(?P<article_id>[0-9]+)$', views.showArticle),
    url('^article$', views.create),
    url('^articles$', views.getJson),
]
