from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("home/", views.home_view, name = "home"),
    path("about/<int:user_id>/", views.about_view, name="about_view"),
    path("flight/", views.passenger_form, name="flight"),
    path("all_flights/", views.flight_view, name="all_flight"),
    path("passengers/<int:flight_id>", views.flight, name="passenger"),
    path("contact/", views.contact, name="contact"),
    path("feedback/", views.feedback_view, name="feedback"),
]