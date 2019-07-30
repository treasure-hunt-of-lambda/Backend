from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room_view, name='room_view'),
    path('player/', views.player_view, name='player_view'),
]