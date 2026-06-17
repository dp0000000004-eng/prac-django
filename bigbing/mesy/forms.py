from django import forms
from .models import Passenger, Feedback

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['message']