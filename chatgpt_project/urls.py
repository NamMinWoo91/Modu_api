from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chat.urls")),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="chat/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    path(
        "accounts/login/", auth_views.LoginView.as_view(template_name="chat/login.html")
    ),  # 이 줄을 추가
]
