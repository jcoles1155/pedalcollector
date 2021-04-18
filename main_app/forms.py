from django.forms import ModelForm
from .models import PlayedAt


class PlayedAtForm(ModelForm):
    class Meta:
        model = PlayedAt
        fields = ['date', 'location', 'show']
