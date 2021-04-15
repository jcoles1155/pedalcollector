from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
from .models import Pedal


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pedals_index(request):
    pedals = Pedal.objects.all()
    return render(request, 'pedals/index.html', {'pedals': pedals})


def pedals_detail(request, pedal_id):
    pedal = Pedal.objects.get(id=pedal_id)
    context = {
        'pedal': pedal
    }
    return render(request, 'pedals/detail.html', context)

# class Pedal:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, type, description, price):
#         self.name = name
#         self.type = type
#         self.description = description
#         self.price = price


# pedals = [
#     Pedal('Fuzzface', 'Overdrive', 'Jimis fav', 300),
#     Pedal('HOF', 'Reverb', 'lots of reverb sounds', 200),
#     Pedal('Boss Compressor', 'Compressor', '10 Band compression', 40)
# ]
