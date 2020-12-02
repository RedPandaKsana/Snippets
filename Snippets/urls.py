"""Snippets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='main_page'),
    path('thanks/', views.thanks),
    path('snippets/add', views.add_snippet_page, name="snippet_add"),
    path('snippets/list', views.snippets_page, name="snippet_list"),
    path('snippet/<int:snippet_id>', views.snippet, name="snippet"),
    path('login/', views.login_page), # ссылка на страницу для входа
    path('auth/', views.login), # прием данных от формы для логина
    path('logout/', views.logout),
    path('snippet/delete/<int:delete_id>', views.delete, name="delete"),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('comment/add', views.comment_add, name='comment_add'),
    path('my_snippets', views.my_snippets, name='my_snippets'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

