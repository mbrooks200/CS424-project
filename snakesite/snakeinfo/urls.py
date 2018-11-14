from django.urls import path
from . import views

urlpatterns = [
            path('', views.snakes),
            path('snake/id/<int:snake_id>', views.snake, name = 'snake_profile'),
            path('snake/update/id/<int:snake_id>', views.snake_update, name = "snake_update"),
]
