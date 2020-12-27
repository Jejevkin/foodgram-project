from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='ingredient name')
    unit = models.CharField(max_length=64,
                            verbose_name='ingredient unit')  # проверить

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.unit}'
