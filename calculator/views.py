from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import CalculatorForm
from .models import Result

# Create your views here.
def calculator_view(request, result = None):
    calculator = CalculatorForm(request.POST or None)
    context = {
        'form': calculator,
        'result': result,
        }
    if request.method == "POST":
        if calculator.is_valid():
            result = calculator.save()
            context['result'] = result.calculate()
    return render(request, "calculator/calculator.html", context)
