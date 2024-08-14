from django.urls import path
from . import views

urlpatterns = [
    path("", views.ChatView.as_view(), name="chat"),  # 기본 URL
    path("chat/", views.ChatView.as_view(), name="chat"),
    path("history/", views.SearchHistoryView.as_view(), name="search_history"),
    # 로그인/로그아웃 URL 등 추가
]
