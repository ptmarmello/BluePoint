"""BluePoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings

from django.urls import path,re_path,include
from ProdCreate import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pwa.urls')),
    url(r'^$', views.userlogin, name='userlogin'),
    url(r'^home/$',views.home,name='home'),
    url(r'^templatepage/',views.radial, name='radial'),
    url(r'^wallet/(?P<name>[\w.@+-]+)/$',views.walletpage, name='walletpage'),
    url(r'^prodlist/',views.listpage, name='prodlist'),
    url(r'^seg/$', views.segloginpage,name='segloginpage'),
    url(r'^seg/formpage/',views.formpage, name='formpage'),
    url(r'^seg/adminpage/',views.adminpage, name='adminpage'),
    url(r'^seg/seglogin/',views.segloginpage,name= 'segloginpage'),
    url(r'^testes/',views.testes,name='testes'),
    url(r'^prodpage/(?P<pk>\d+)/$',views.productpage,name='prodpage'),
    url(r'^userlogin/',views.userlogin,name='userlogin'),
    url(r'^userconfig/(?P<name>[\w.@+-]+)/$',views.configpage, name='userconfig'),
    url(r'^onboarding/',views.onboarding,name='onboarding'),
    url(r'^quizpage/',views.quizpage,name='quizpage'),
    url(r'^quizpage_2/',views.quizpage_2,name='quizpage_2'),
    url(r'^quizpage_3/',views.quizpage_3,name='quizpage_3'),
    url(r'^quizpage_4/',views.quizpage_4,name='quizpage_4'),
    url(r'^quizpage_5/',views.quizpage_5,name='quizpage_5'),


    #(?P<pk>[\w.@+-]+)/$



]

urlpatterns +=staticfiles_urlpatterns()
