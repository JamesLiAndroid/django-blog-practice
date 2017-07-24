#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from blog.feeds import AllPostsRssFeed
from . import views

app_name = 'blog' # 指定视图函数的命名空间
urlpatterns = [

    # 类视图转换成函数视图非常简单，需调用类视图的 as_view()
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^$', views.index, name='index'), # 正则表达式，匹配一个空字符串


    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail' ),


    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    #    url(r'^archives/(?P<year>[0-9]{4})/(P<month>[0-9]{1,2})/$', views.archives, name='archives')

    #url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category')
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),

    # 标签云视图
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

    # RSS订阅
#    url(r'^all/rss/$', AllPostsRssFeed(), name='rss')
]
