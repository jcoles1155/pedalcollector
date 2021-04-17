from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Define the home view
from .models import Pedal

from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


class PedalCreate(CreateView):
    model = Pedal
    fields = '__all__'
    success_url = '/pedals/'


class PedalUpdate(UpdateView):
    model = Pedal
  # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['name', 'type', 'description', 'price']


class PedalDelete(DeleteView):
    model = Pedal
    success_url = '/pedals/'
