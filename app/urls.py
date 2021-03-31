from django.urls import path

from . import views


app_name = 'app'

urlpatterns = [
    path('registration/', views.CreateUserView.as_view(), name='registration'),
    path('login/', views.CreateTokenView.as_view(), name='login'),
]