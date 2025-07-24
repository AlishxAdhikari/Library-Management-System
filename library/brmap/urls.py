"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.urls import include,re_path
from .views import  addBookView, addBook,  deleteBook,aboutView, helpview, contactView, user_login, user_logout, home
from .views import viewBook, edit_book


urlpatterns = [
   path('', home, name='home'),
   path('view-book/', viewBook, name='view-book'),
   path('add-book/',addBookView),
   path("add-book/add/", addBook),

   path("edit-book/edit/", edit_book),
  path('edit-book/delete/', deleteBook, name='delete-book'),
  path('about/', aboutView, name='about'),
  path('help/', helpview, name='help'),
  path('contact/',contactView, name='contact'),
  path('login/', user_login, name='login'),
  path('logout/', user_logout, name='logout'),
  path('home/', home, name='home'),
]

   

