from django.urls import path
from . import views

urlpatterns = [
            path('', views.snakes),
            path('snake/id/<int:snake_id>', views.snake)
]
