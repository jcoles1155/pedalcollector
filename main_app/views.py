from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

# Define the home view
from .models import Pedal, Instrument, Photo

from .forms import PlayedAtForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

import uuid
import boto3

S3_BASE_URL = 's3-us-west-1.amazonaws.com'
BUCKET = 'pedalcollector'


class PedalCreate(CreateView):
    model = Pedal
    fields = ['name', 'type', 'description', 'price']

    # valid pedal form is being submitted
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the pedal
        # Let the CreateView do its job as usual
        return super().form_valid(form)


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

@login_required
def pedals_index(request):
    pedals = Pedal.objects.filter(user=request.user)
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


def add_photo(request, pedal_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to pedal_id or pedal (if you have a pedal object)
            photo = Photo(url=url, pedal_id=pedal_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('details', pedal_id=pedal_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)