from django.shortcuts import render
from django.views.generic.list import ListView

from snakeinfo.models import Snake
from django.http import HttpResponse

def snake(request, snake_id):
    snake = Snake.objects.get(id=snake_id)
    response = render(request, "snakeinfo/snake_detail.html", {
        "snake" : snake
        })
    return response


def snakes(request):
    output = []
    snakelist = Snake.objects.all()

    output = "<br>".join([("Name: " + i.name + ", &emsp;" + "Average Lifespan in Captivity (Years): " + str(i.avg_lifespan_years) + ", &emsp;" + "Skill Level Needed to Keep: " +i.skill_level + ", &emsp;" + "Temperatures Required: " + i.temp_requirement) for i in snakelist])
    return HttpResponse(output)