from django.shortcuts import render
from .forms import PassengerForm
from .models import Flight, Passenger
from django.shortcuts import get_object_or_404
# Create your views here.


def passenger_form(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = PassengerForm
    
    return render(request, "mesy/flight.html", {"form":PassengerForm(request.POST)})


def flight_view(request):
    flights = Flight.objects.all()
    return render(request, "mesy/all_flight.html", {"flights":flights})


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    return render(request, "mesy/passenger.html", {"flight":flight, "passengers":passengers})