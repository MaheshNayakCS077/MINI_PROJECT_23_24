from django import forms
from .models import Data


class inputForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['ID', 'Name', 'DOB']
        widgets = {
            'DOB': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
        }
