from datetime import (
    date,
)

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from abstracts.models import DateTimeCustom


def validate_exercise_deadline(deadline: date) -> None:  # noqa
    today: date = date.today()
    if deadline < today:
        raise ValidationError(
            "You can not organize exercise in past",
            code="past_deadline_error"
        )


class Exercise(DateTimeCustom):  # noqa
    finish_date_deadline = models.DateField(
        verbose_name='Заданное время выполнения',
        validators=[validate_exercise_deadline]
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
        return f'Задание для пользователя {self.user.username}'
