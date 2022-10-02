from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRoutes, name="getRoutes"),
    path('users/', views.getUsers, name="getUsers"),
    path('user/<str:pk>/', views.getUser, name="getUsers"),
    path('user/<str:pk>/categories', views.getUserCategories, name="getUserCategories"),
    path('user/<str:pk>/todos', views.getUserTodos, name="getUserTodos"),
    #path('user/<str:pk>/todo/<str:pk2>', views.getUserTodo, name="getUserTodo"),
]
