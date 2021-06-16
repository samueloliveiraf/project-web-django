
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user),
    path('registrar/', views.SignUp.as_view(), name="signup"),
]
