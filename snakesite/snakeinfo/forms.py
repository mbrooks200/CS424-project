from django import forms
from snakeinfo.models import Snake

class SnakeForm(forms.ModelForm):
    class Meta:
        model = Snake
        exclude = []
