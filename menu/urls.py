"""
URL configuration for dugoutmenu project.

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
from django.urls import path,include
from .import views

app_name="menu"
urlpatterns = [
    path('', views.menu_view, name='menu'),
    
    # Dashboard URLs
    path('dashboard/login/', views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    path('dashboard/item/add/', views.dashboard_item_create, name='dashboard_item_create'),
    path('dashboard/item/<int:pk>/edit/', views.dashboard_item_update, name='dashboard_item_update'),
    path('dashboard/item/<int:pk>/delete/', views.dashboard_item_delete, name='dashboard_item_delete'),
    path('dashboard/category/add/', views.dashboard_category_create, name='dashboard_category_create'),
    path('dashboard/category/<int:pk>/edit/', views.dashboard_category_update, name='dashboard_category_update'),
    path('dashboard/category/<int:pk>/delete/', views.dashboard_category_delete, name='dashboard_category_delete'),
]

