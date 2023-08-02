from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'Code: {self.code} <br> Country: <b>{self.name}</b>'
    