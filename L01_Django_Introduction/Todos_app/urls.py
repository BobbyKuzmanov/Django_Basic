from django.urls import path

from djangoProject.todos.views import index

urlpatterns = [
    path('', index),
]
