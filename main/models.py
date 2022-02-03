from django.db import models

class Country (models.Model):
    name = models.CharField('Название страны', max_length=20)
    population = models.CharField('Насиление', max_length=20)
    presidents = models.CharField('Президент', max_length=20)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
