from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('chatbot/', views.chatbot, name='chatbot'),
  path("dashboard/", views.operator_dashboard, name="operator_dashboard"),
  path("get_chat_history/", views.get_chat_history, name="get_chat_history"),
]
