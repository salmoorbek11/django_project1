from django.db import models
from django import forms

class ToDo(models.Model):
    name = models.CharField('Название действия', max_length=255)
    is_done = models.BooleanField('Выполнено', default=False)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    name = models.CharField(max_length=20)