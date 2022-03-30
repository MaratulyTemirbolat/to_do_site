from django.urls import path

from to_do.views import (
    MainView,
    CreateExerciseView,
)

urlpatterns = [
    path('', MainView.as_view(), name="main_page"),
    path('add_exercise/', CreateExerciseView.as_view(), name="add_exercise")
]
