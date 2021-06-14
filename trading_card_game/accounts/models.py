from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
from trading_outpost.models import Queens, My_Card
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.user.username)

@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        card_queen= Queens.objects.all()
        random_queens= random.sample(list(card_queen), 20)
        for queen in random_queens:
            My_Card.objects.create(queen = queen, profile=profile)
        #     #Assigning my queen model to queen for loop

