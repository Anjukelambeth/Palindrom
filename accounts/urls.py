
from django.urls import path
from .api import RegisterApi
from . import views

urlpatterns = [
  path('api/register', RegisterApi.as_view()),
  path('hello/', views.HelloView.as_view(), name ='hello'),
  # path('allUser/',views.allUser),
  path('allUser/', views.AllUser.as_view(), name ='allUser'),
  path('delete/<int:pk>',views.DeleteUser.as_view()),
  path('edit/<int:pk>', views.EditUser.as_view()),
  path('adduser/', views.NewUserAdd.as_view()),
  path('gamestart/', views.GameStart.as_view()),
  path('getboard/', views.GetBoard.as_view()),
  path('getmyallgame/', views.GameList.as_view()),
  path('allgame/', views.GameListAll.as_view()),
]