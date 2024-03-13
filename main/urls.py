from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # 글 작성 페이지를 위한 URL
]
