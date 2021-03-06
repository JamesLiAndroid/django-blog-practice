#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = 'blog' # 指定视图函数的命名空间
urlpatterns = [
    # url(r'^$', views.index, name='index'), # 正则表达式，匹配一个空字符串
    url(r'^$', views.IndexView.as_view(), name='index') # 类视图
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail' ),

    #url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]{1,2}/$)', views.ArchivesView.as_view(), name='archives')
    # url(r'^archives/(?P<year>[0-9]{4})/(P<month>[0-9]{1,2})/$', views.archives, name='archives')

    #url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category')
]
