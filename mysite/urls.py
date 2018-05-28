"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from api import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^exam1/$',views.exam1.as_view()),
    url(r'^exam2/$',views.exam2.as_view()),
    url(r'^exam3/$',views.exam3.as_view()),
    url(r'^exam4/$',views.exam4.as_view()),
    url(r'^exam5/$',views.exam5.as_view()),
    url(r'^general_science/$',views.general_science.as_view()), 
    url(r'^current_affairs/$',views.current_affairs.as_view()),
    url(r'^english/$',views.english.as_view()),   
]
