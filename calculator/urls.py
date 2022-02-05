from django.urls import path
from .views import calculator_view

app_name = 'calculator'
urlpatterns = [
    path(route='', view=calculator_view, name='calculator'),
]