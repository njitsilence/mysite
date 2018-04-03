from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('daily_check',views.daily_check,name='daily_check')
]