from typing import (
    Type,
    Tuple,
    Dict,
    Any,
)

from django import forms

from to_do.models import (
    Exercise,
)


class ExerciseCreationForm(forms.ModelForm):  # noqa
    class Meta:  # noqa
        model: Type[Exercise] = Exercise
        fields: Tuple[str] = (
            'finish_date_deadline', 'user',
            'description', 'activity',
        )
