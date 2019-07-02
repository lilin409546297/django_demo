from django.conf.urls import url

from django_demo import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^role/(?P<userId>\d+)$', views.role, name="role"),
    url(r'^role2$', views.role2, name="role2"),
]
