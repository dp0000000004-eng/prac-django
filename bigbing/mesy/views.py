from django.shortcuts import render, redirect
from .forms import PassengerForm, FeedbackForm
from .models import Flight, Feedback
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required

# Create your views here.



def passenger_form(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = PassengerForm
    
    return render(request, "mesy/flight.html", {"form":PassengerForm(request.POST)})


@login_required
def flight_view(request):
    flights = Flight.objects.all()
    return render(request, "mesy/all_flight.html", {"flights":flights})


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    return render(request, "mesy/passenger.html", {"flight":flight, "passengers":passengers})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, message="Invalid Username or password")
    return render(request, 'mesy/login.html')

@login_required
def home_view(request):
    return render(request, "mesy/index.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def contact(request):
    return render(request, "mesy/contact.html")

@login_required
def about_view(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, message="Thanks For Feedback:)")
        else:
            form = FeedbackForm()

    return render(request, "mesy/about.html", {"form":FeedbackForm(request.POST) , "user":user})


@login_required
def feedback_view(request):
    feedback = Feedback.objects.all()
    return render(request, "mesy/feedbacks.html", {"feedbacks":feedback})