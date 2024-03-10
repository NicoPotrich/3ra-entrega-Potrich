from django.forms import DateTimeInput, ModelForm
from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = "__all__"
        widgets = {
            'date_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'estimated_end': DateTimeInput(attrs={'type': 'datetime-local'})
        }

