from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class GameRating(models.Model):
    """Database model for a game rating"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
<<<<<<< HEAD
    created_on = models.DateField()
=======
    created_on = models.DateField()
>>>>>>> 7fbab2b (Created remaining needed files and updated files based on GitHub files)
