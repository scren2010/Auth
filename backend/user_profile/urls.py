from django.urls import path

from backend.user_profile import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('profile/', views.ProfileView.as_view()),
]
