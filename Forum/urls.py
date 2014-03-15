# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from Forum import views

urlpatterns = patterns('',
    # Base forum
    url(r'^$', views.forum, name='base_forum'),
    url(r'^page/(?P<page>\d+)/$', views.forum),
    # Subforums
    url(r'^subforum/(?P<subforum_id>\d+)[\w\d@\.\+\-_]*/$', views.subforum, name='subforum'),
    url(r'^subforum/(?P<subforum_id>\d+)[\w\d@\.\+\-_]*/page/(?P<page>\d+)/$', views.subforum, name='subforum'),
    url(r'^subforum/(?P<subforum_id>\d+)[\w\d@\.\+\-_]*/post/$', views.newThread),
    url(r'^subforum/(?P<subforum_id>\d+)[\w\d@\.\+\-_]*/new-subforum/$', views.newSubforum),
    # Threads
    url(r'^thread/(?P<thread_id>\d+)[\w\d@\.\+\-_]*/page/last/$', views.threadLastPage, name='thread_last_page'),
    url(r'^thread/(?P<thread_id>\d+)[\w\d@\.\+\-_]*/page/last-read/$', views.lastPostReadThread),
    url(r'^thread/(?P<thread_id>\d+)[\w\d@\.\+\-_]*/$', views.thread, name='thread'),
    url(r'^thread/(?P<thread_id>\d+)[\w\d@\.\+\-_]*/page/(?P<page>\d+)/$', views.thread),
    url(r'^thread/(?P<thread_id>\d+)[\w\d@\.\+\-_]*/page/(?P<page>\d+)/#(?P<post_id>\d+)$', views.thread),
    url(r'^thread/(?P<thread_id>\d+)[\w\d@\.\+\-_]*/post/$', views.replyThread),
    # Posts
    url(r'^post/(?P<post_id>\d+)/$', views.post),
    url(r'^post/(?P<post_id>\d+)/edit/$', views.editPost),
    url(r'^post/(?P<post_id>\d+)/report/$', views.reportPost),
    url(r'^post/(?P<post_id>\d+)/quote/$', views.quotePost),
    #System
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),

)
