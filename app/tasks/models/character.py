from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Character(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='character'
    )
    health = models.PositiveIntegerField(default=100)
    strength = models.PositiveIntegerField(default=10)
    dexterity = models.PositiveIntegerField(default=10)
    intelligence = models.PositiveIntegerField(default=10)
    experience = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    
    # Gamification methods
    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()
        self.save()

    def check_level_up(self):
        if self.experience >= self.level * 100:
            self.level += 1
            self.strength += 2
            self.dexterity += 2
            self.health += 10
            return True
        return False

    def __str__(self):
        return f"{self.user.username}'s character (Lv.{self.level})"

# Auto-create character when user registers
@receiver(post_save, sender=User)
def create_character(sender, instance, created, **kwargs):
    if created:
        Character.objects.create(user=instance)
