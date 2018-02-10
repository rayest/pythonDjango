from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^lee$', views.index),
    url('^ray', views.showRay),
]
