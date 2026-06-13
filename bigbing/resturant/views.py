
from django import forms
from django.shortcuts import render
from .models import BookForm

# Create your views here.

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookForm
        fields = '__all__'


def reservation(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = BookingForm()

    return render(request, "resturant/book.html", {"form":BookingForm()})