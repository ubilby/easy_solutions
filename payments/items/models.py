from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=80, blank=False)
    description = models.CharField(verbose_name='Описание', max_length=500)
    price = models.DecimalField(
        verbose_name='Цена', max_digits=10, decimal_places=2
    )
