from django.urls import path
from .views import ListTodo,DetailTodo,CreateTodo

urlpatterns = [
    path('<int:pk>/',DetailTodo.as_view()),
    path('',ListTodo.as_view()),
    path('new/',CreateTodo.as_view())
]

