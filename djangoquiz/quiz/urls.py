from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home, name='quiz-home'),
    path('register/', views.register,name='quiz-register'),
    path('login/', auth_views.LoginView.as_view(template_name='quiz/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='quiz/logout.html'), name='logout'),
    path('math_quiz/', views.math_view, name="quiz-math_view"),
    path('stat_quiz/', views.stat_view, name="quiz-stat_view"),
]
