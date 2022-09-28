"""libraryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from libraryapp.views import UserViewSet, GroupViewSet, add_book, register_new_admin, login_new_admin, register_new_user, login_new_user, get_all_books_by_user, modify_book_details, get_all_books_by_admin, delete_item


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('add_book/',add_book),
    path('register_new_admin/',register_new_admin),
    path('login_new_admin/', login_new_admin),
    path('register_new_user/', register_new_user),
    path('login_new_user/', login_new_user),
    path('get_all_books_by_user/', get_all_books_by_user),
    path('modify_book_details/', modify_book_details),
    path('get_all_books_by_admin/', get_all_books_by_admin),
    path('delete_item/',delete_item),
]
