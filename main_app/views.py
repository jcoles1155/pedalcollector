from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

# Define the home view
from .models import Pedal

from .models import Instrument

from .forms import PlayedAtForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def pedals_index(request):
    pedals = Pedal.objects.all()
    return render(request, 'pedals/index.html', {'pedals': pedals})


def pedals_detail(request, pedal_id):
    pedal = Pedal.objects.get(id=pedal_id)
    instruments_pedal_doesnt_have = Instrument.objects.exclude(
        id__in=pedal.instruments.all().values_list('id'))
    playedat_form = PlayedAtForm()
    return render(request, 'pedals/detail.html', {
        # include the pedal and playedat_form in the context
        'pedal': pedal, 'playedat_form': playedat_form,

        'instruments': instruments_pedal_doesnt_have
    })


def add_show(request, pedal_id):
    # create the ModelForm using the data in request.POST
    form = PlayedAtForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_show = form.save(commit=False)
        new_show.pedal_id = pedal_id
        new_show.save()
        print(new_show)
    return redirect('details', pedal_id=pedal_id)


# Instruments Views
def instruments_index(request):
    instruments = Instrument.objects.all()
    context = {'instruments': instruments}

    return render(request, 'instrument/index.html', context)


def instrument_detail(request, instrument_id):
    instrument = Instrument.objects.get(id=instrument_id)
    context = {
        'instrument': instrument
    }
    return render(request, 'instrument/detail.html', context)


class Create_instrument(CreateView):
    model = Instrument
    fields = '__all__'


class Update_instrument(UpdateView):
    model = Instrument
    fields = ['color']


class Delete_instrument(DeleteView):
    model = Instrument
    success_url = '/instruments/'


def assoc_instrument(request, pedal_id, instrument_id):
    # Note that you can pass a instrument's id instead of the whole object
    Pedal.objects.get(id=pedal_id).instruments.add(instrument_id)
    return redirect('details', pedal_id=pedal_id)
