from django.urls import path
from app1 import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('index/calc/page', views.index_view, name='index'),
]
