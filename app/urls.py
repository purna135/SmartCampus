from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('irrigation/', views.smart_irrigation, name='irrigation'),
    path('bells/', views.smart_bell, name='bells'),
    path('notice_board/', views.smart_notice_board, name='notice_board'),
    path('attendance/', views.smart_attendance, name='attendance'),
    path('add/', views.add, name='add'),
]
