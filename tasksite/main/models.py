from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    title = models.CharField("Название",max_length=200)
    task=models.TextField("Описание")
    checking=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"


