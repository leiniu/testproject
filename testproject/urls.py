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
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from testapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/index/$', index,name='index'),
    url(r'^testtest/$', test),
    url(r'^test/$', login_view,name='login'),
    #url(r'^test/login', login_view),
    url(r'test/logout',logout_view,name='logout'),
    url(r'^test/(\d+)/case/$', get_case_list,name='case_list'),
    url(r'^test/prd/$', get_prd_list,name='prd_list'),
    url(r'^test/article/all/$', get_article_list,name='article_list'),
    url(r'^test/article/personal/(\D+)$', get_personal_article_list,name='personal_article_list'),
    url(r'^test/(\d+)/case/add/', add_case,name='add_case'),
    url(r'^test/prd/add/', add_prd,name='add_prd'),
    url(r'^test/article/add/', add_article,name='add_article'),
    url(r'^test/case/(\d+)/$', case_detail, name='case_detail'),
    url(r'^test/case/(\d+)/change', change_case, name='change_case'),
    url(r'^test/case/(\d+)/delete', delete_case, name='delete_case'),
    url(r'^test/article/(\d+)/$', article_detail, name='article_detail'),
    url(r'^test/article/(\d+)/delete', delete_article, name='delete_article'),
    url(r'^test/article/(\d+)/change', change_article, name='change_article'),
    url(r'^test/prd/(\d+)/change$', change_prd, name='change_prd'),
    url(r'^test/search$',search),
    url(r'test/upload',upload,name='upload'),
    url(r'^media/(?P<path>.*)$',  serve,  {'document_root':settings.MEDIA_ROOT,}),
]
