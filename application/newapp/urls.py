"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from newapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('userlogin', views.userlogin),
    #path('data', views.data),
    path('logout', views.userlogout),
    path('add', views.add),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('show', views.show),
    path('newuser', views.newuser),
    path('contact', views.contact),
    path('about', views.about),
    path('service', views.service),
    path('mail/<int:id>', views.mail),
]
