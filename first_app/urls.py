from django.urls import path
from . import views

urlpatterns = [
  path('<topic>/', views.news_view)
]