from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    budget = models.IntegerField(default=0)

    def __str__(self):
        return self.user_name

class Pet(models.Model):
    user = models.ForeignKey(User)
    pet_name = models.CharField(max_length=200)
    pet_health = models.IntegerField(default=100)
    virtual_gold = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.pet_name
