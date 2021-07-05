from django.conf.urls import url
from django.urls import path 
from . import views

urlpatterns=[
    path('games/', views.game_list),
    path('games/<int:pk>', views.game_detail),
]