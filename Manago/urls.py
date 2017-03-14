"""Manago URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from manago.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Manago/', home_request),
    url(r'admin_login/',admin_login),
    url(r'client_verify/',client_entries),
    url(r'developer_verify/',developer_entries),
    url(r'developer_login/',developer_login),
    url(r'client_login/',client_login),
    url(r'developer_panel/',developer_panel),
    url(r'client_panel/',client_panel),
    url(r'all_docs/',all_docs),
]
