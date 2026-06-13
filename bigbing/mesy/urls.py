from django.urls import path
from . import views


urlpatterns = [
    path("flight/", views.passenger_form, name="flight"),
    path("all_flights/", views.flight_view, name="all_flight"),
    path("passengers/<int:flight_id>", views.flight, name="passenger")
]