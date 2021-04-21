from django.db import models

from django.urls import reverse

# Create your models here.

SHOWS = (
    ('A', 'Acoustic'),
    ('R', 'Rock'),
    ('J', 'Jazz')
)


class Instrument(models.Model):
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.type} {self.brand} {self.make}'

    def get_absolute_url(self):
        return reverse('instrument_detail', kwargs={'instrument_id': self.id})

        class Meta:
            ordering = ['-date']


class Pedal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'pedal_id': self.id})


class PlayedAt(models.Model):
    date = models.DateField('show date')
    location = models.TextField(max_length=250)
    show = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=SHOWS,
        # set the default value for meal to be 'B'
        default=SHOWS[0][0]
    )

    pedal = models.ForeignKey(Pedal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_show_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
