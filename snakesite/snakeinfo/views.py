
from django.shortcuts import render

from django.contrib.auth.models import User

from django.views.generic.list import ListView

from django.urls import reverse

from snakeinfo.models import Snake

from django.http import HttpResponse, HttpResponseRedirect

from snakeinfo.forms import SnakeForm

from django.contrib.auth.decorators import login_required

def snake(request, snake_id):
    snake = Snake.objects.get(id=snake_id)
    response = render(request, "snakeinfo/snake_detail.html", {
        "snake" : snake
        })
    return response


def snakes(request):
    snakes = Snake.objects.all()
    response = render(request, "snakeinfo/snake_list.html", {
        "snakes": snakes})
    return response

@login_required
def snake_update(request, snake_id):
    snake = Snake.objects.get(id = snake_id)
    if snake.user == request.user.id:  # I know snake.user does not access the user, but not sure how to fix.
        if request.method == "POST":
            form = SnakeForm(request.POST, instance = snake)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("snake_profile", kwargs={"snake_id": snake_id}))
            else:
                return HttpResponseRedirect("/")
        form = SnakeForm()
        return render(request, "snakeinfo/snake_update.html", {
        "form" : form
        })
    else:
        return render(request, "snakeinfo/no_permission.html", {})