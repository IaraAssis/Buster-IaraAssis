from django.urls import path
from .views import UserView, UserDetailView
from movies.views import LoginJWTView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    # URLs relacionadas ao usuário
    path("users/", UserView.as_view(), name="user-create"),
    path("users/<int:user_id>/", UserDetailView.as_view(), name="detail-view"),

    # Rotas de autenticação
    path(
        "users/login/",
        LoginJWTView.as_view(),
        name="token-obtain-pair",
    ),
    path(
        "users/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token-refresh",
    ),
]
