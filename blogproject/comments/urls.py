#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name='comments'
urlpatterns = [
    url('^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]
