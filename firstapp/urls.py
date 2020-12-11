from django.urls import path

from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('news', views.news, name='news'),
	path('news/create', views.news_create, name='news_create'),
	path('news/<int:pk>', views.news_detail, name='news_detail'),
	path('news/<int:pk>/delete', views.news_delete, name='news_delete'),
]