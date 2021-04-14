from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def pedals_index(request):
    return render(request, 'pedals/index.html', {'pedals': pedals})


class Pedal:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, type, description, price):
        self.name = name
        self.type = type
        self.description = description
        self.price = price


pedals = [
    Pedal('Fuzzface', 'Overdrive', 'Jimis fav', 300),
    Pedal('HOF', 'Reverb', 'lots of reverb sounds', 200),
    Pedal('Boss Compressor', 'Compressor', '10 Band compression', 40)
]
