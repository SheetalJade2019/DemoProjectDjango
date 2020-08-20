from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.todoView, name="todo"),
    path('addTodo/',views.addTodo, name="addTodo"),
    path('deleteTodo/<int:todo_id>/', views.deleteTodo, name='deleteTodo'),
]
