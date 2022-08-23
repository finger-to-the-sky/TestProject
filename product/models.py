from django.db import models

class Product(models.Model):
    header = models.CharField(max_length=64)
    text = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f'Товар {self.header} | Стоимость {self.text}'
