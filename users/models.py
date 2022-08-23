from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    email = models.EmailField(blank=True, unique=True)

    def __str__(self):
        return f'Пользователь {self.username}'

class AccountBalance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return f'Баланс: {self.balance}'
