from django.db import models

class Recipe(models.Model):
    
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    total_time = models.DurationField()
