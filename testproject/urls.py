"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from testapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^testtest/$', test),
    url(r'^test/$', login_view),
    #url(r'^test/login', login_view),
    url(r'test/logout',logout_view),
    url(r'^testapp/(\d+)/case/$', get_case_list,name='case_list'),
    url(r'^testapp/prd/$', get_prd_list),
    url(r'^testapp/article/all/$', get_article_list),
    url(r'^testapp/article/personal/(\D+)$', get_personal_article_list),
    url(r'^testapp/case/add/', addcase),
    url(r'^testapp/prd/add/', addprd),
    url(r'^testapp/article/add/', addarticle),
    url(r'^testapp/case/(\d+)/$', case_detail, name='case_detail'),
    url(r'^testapp/case/(\d+)/change', change_case, name='change_case'),
    url(r'^testapp/case/(\d+)/delete', delete_case, name='delete_case'),
    url(r'^testapp/article/(\d+)/$', article_detail, name='article_detail'),
    url(r'^testapp/article/(\d+)/delete', delete_article, name='delete_article'),
    url(r'^testapp/article/(\d+)/change', change_article, name='change_article'),
    url(r'^testapp/prd/(\d+)/change$', change_prd, name='change_prd'),
    url(r'^testapp/search$',search),
]
