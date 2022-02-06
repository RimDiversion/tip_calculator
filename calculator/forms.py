from django.forms import ModelForm
from .models import Result

class CalculatorForm(ModelForm):
    class Meta:
        model = Result
        fields = ['amount', 'tip_percent']