#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = 'blog' # 指定视图函数的命名空间
urlpatterns = [
    url(r'^$', views.index, name='index'), # 正则表达式，匹配一个空字符串
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail' )
]
