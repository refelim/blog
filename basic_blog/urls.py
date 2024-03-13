from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'), 
    path('write/', views.post_write, name='post_write'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('search/<str:tags>/', views.post_search, name='post_search'),
 ] 
