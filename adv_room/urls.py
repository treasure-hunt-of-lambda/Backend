from django.urls import path

from adv_room import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room_view.as_view()),
    path('player/', views.player_view.as_view()),
]