"""
URL configuration for demoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    # whenever someone runs the app, the urls file in demoProject redirects user to this file when url is empty
    # then the empty path will load homepage function present in views file
    path("",views.homepage,name="homepage"),
    path("register/",views.register,name="register"),
    path("logout/",views.logout_request,name="logout"),
    path("login/",views.login_request,name="logout"),
    path("<single_slug>",views.single_slug,name="single_slug"),
]
