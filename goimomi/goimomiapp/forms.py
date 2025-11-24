from django import forms # pyright: ignore[reportMissingModuleSource]
from .models import ContactMessage, CustomizedHoliday, CustomizedUmrah

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class CustomizedHolidayForm(forms.ModelForm):
    class Meta:
        model = CustomizedHoliday
        fields = ['name', 'email', 'phone', 'destination', 'start_date', 'end_date', 'message']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }

class CustomizedUmrahForm(forms.ModelForm):
    class Meta:
        model = CustomizedUmrah
        fields = ['name', 'email', 'phone', 'package_type', 'travel_date', 'message']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
