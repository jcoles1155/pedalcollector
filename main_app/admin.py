from django.contrib import admin

# Register your models here.
from .models import Instrument, Pedal, PlayedAt, Instrument

admin.site.register(Pedal)

admin.site.register(PlayedAt)

admin.site.register(Instrument)
