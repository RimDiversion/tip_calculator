from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def calculator_view(request):
    context = {}
    return render(request, "calculator/calculator.html", context)