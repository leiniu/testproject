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
    url(r'^index/', index),
    url(r'^testapp/login', login),
    url(r'^testapp/prd/(\d+)/case$', get_case_list,name='case_list'),
    url(r'^testapp/prd$', get_prd_list),
    url(r'^testapp/case/add/', addcase),
    url(r'^testapp/prd/add/', addprd),
    url(r'^testapp/case/(\d+)/change', case_detail, name='case_detail'),
    url(r'^testapp/prd/(\d+)/change', prd_detail, name='prd_detail'),
]
