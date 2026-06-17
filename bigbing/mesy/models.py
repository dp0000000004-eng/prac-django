from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} {self.code}"
    
class Flight(models.Model):
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name="depature")
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} -> {self.destination} {self.duration}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    flight = models.ManyToManyField(Flight, related_name = "passengers", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_feedback")
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.message} - {self.created_at[:30]}"