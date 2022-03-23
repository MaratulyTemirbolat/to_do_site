from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from abstracts.models import DateTimeCustom


class Exercise(DateTimeCustom):  # noqa
    finish_date_deadline = models.DateField(
        verbose_name='Заданное время выполнения'
    )
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        verbose_name='Пользователь'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    activity = models.BooleanField(
        verbose_name='Активность',
        default=True
    )

    class Meta:  # noqa
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['id', ]

    def __str__(self) -> str:  # noqa
        return f'Домашка пользователя {self.user.username}'
