from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        return f'{name.upper()}'

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'count', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name',
                                           'data-rule': 'minlen:4'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email',
                                             'data-rule': 'minlen:4'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone',
                                            'data-rule': 'minlen:4'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'id': 'date', 'placeholder': 'Date',
                                           'data-rule': 'minlen:4'}),
            'time': forms.TextInput(attrs={'class': 'form-control', 'id': 'time', 'placeholder': 'Time',
                                           'data-rule': 'minlen:4'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'id': 'people', 'placeholder': 'Number of people',
                                              'data-rule': 'minlen:4'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Comment'})

        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'date': 'Date',
            'time': 'Time',
            'count': 'Number of people',
            'comment': 'Comment'
             }
        help_texts = {
            'name': 'Please enter Your Name',
            'email': 'Please enter a valid email',
            'phone': 'Please enter Your Phone in format: +999999999',
            'date': 'Please enter booking date',
            'time': 'Please enter time',
            'count': 'Please enter comment',
        }
        error_messages = {
            'name': {
                'required': 'This field is required',
            },
            'phone': {
                'required': 'This field is required',
            },
            'email': {
                'required': 'This field is required',
            },
            'date': {
                'required': 'This field is required',
            },
            'time': {
                'required': 'This field is required',
            },
            'count': {
                'required': 'This field is required',
            },
        }