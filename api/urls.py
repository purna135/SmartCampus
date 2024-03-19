import django


from django.urls import path
from . import views

urlpatterns = [
    path('add_irrigation_data/', views.add_irrigation_data, name='add_irrigation_data'),
]
