from django.urls import path
from . import views


urlpatterns = [
    path('', views.chathome, name='chathome'),
    path('<room_name>/', views.activeroom, name='activeroom'),
]