# models.py
from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    result_name = models.CharField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        # Логика для автоматического заполнения result_name при сохранении
        self.result_name = self.first_name + ' ' + self.second_name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Клиент - {self.result_name}'
# Инструкция для модели
# При сохранении экземпляра модели Client, поле result_name будет автоматически создаваться
# как результат конкатенации first_name и second_name. Это поле нельзя редактировать напрямую,
# оно будет изменяться только при вызове метода save или update.

class NotariusService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return f'Нотариальная услуга {self.title}'

# Инструкция для модели
# Модель NotariusService имеет связь ManyToMany с моделью Client.
# Это означает, что каждая услуга может быть связана с несколькими клиентами, и наоборот.