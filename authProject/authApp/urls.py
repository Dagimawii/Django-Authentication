from django.urls import path
from. import views


urlpatterns = [
    path('' , views.home_view, name = 'home'),
    path('login/', views.Login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.Register_view, name = 'register'),
    path('protected/', views.ProtectedView.as_view(), name = 'protected'),
]