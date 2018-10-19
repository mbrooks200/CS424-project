from django.db import models

class Snake(models.Model):
    name = models.CharField(max_length = 50)
    avg_lifespan_years = models.IntegerField()
    skill_level = models.CharField(max_length = 50)
    temp_requirement = models.CharField(max_length = 50)
