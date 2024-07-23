from django.urls import path,include
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('fertilizer/', views.ferti, name='fertilizer'),
    path('fertilizer/predict/', views.predict, name='result'),
]