from django.contrib import admin

# Register your models here.
from .models import Instrument, Pedal, PlayedAt, Photo

admin.site.register(Pedal)

admin.site.register(PlayedAt)

admin.site.register(Instrument)

admin.site.register(Photo)
