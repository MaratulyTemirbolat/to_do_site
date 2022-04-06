from typing import (
    Type,
    Any,
    Dict,
)

from django.views.generic import (
    ListView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from to_do.models import Exercise
from to_do.forms import ExerciseCreationForm


class MainView(ListView):  # noqa
    model: Type[Exercise] = Exercise
    template_name: str = 'to_do/to_do.html'
    context_object_name: str = 'to_do_list'

    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:  # noqa
        context: Dict[str, Any] = super().get_context_data(**kwargs)
        context['title'] = 'Страница заданий'
        return context


class CreateExerciseView(LoginRequiredMixin, CreateView):  # noqa
    raise_exception: bool = True
    form_class = ExerciseCreationForm
    template_name: str = 'to_do/created.html'
    success_url = reverse_lazy('main_page')
