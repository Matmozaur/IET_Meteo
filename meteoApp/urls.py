from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('basic_plot/', views.basic_plot, name='basic_plot'),
    path('add_trend/', views.add_trend, name='add_trend'),
    path('add_stats/', views.add_stats, name='add_stats'),
]
