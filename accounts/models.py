from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GameManager(models.Manager):
    def create_game(self,game_id,game_string,user):
        game=self.model(game_id=game_id,game_string=game_string,user=user)
        game.save(using=self._db)
        return game

class Game(models.Model):
    game_id = models.AutoField(primary_key = True,serialize = False, verbose_name ='ID')
    game_string=models.CharField(max_length=6,default='')
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.game_id 

    objects = GameManager()