from . import views
from authentication.api import views as api_view
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

app_name = 'api'


urlpatterns = [
    path('register/', api_view.RegisterView.as_view(), name="register"),
    path('login/', api_view.LoginAPIView.as_view(), name="login"),
    path('logout/', api_view.LogoutAPIView.as_view(), name="logout"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]