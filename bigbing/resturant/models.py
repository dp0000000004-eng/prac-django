from django.db import models

# Create your models here.

class BookForm(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    guest_count = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.firest_name} {self.last_name} {self.guest_count} {self.comment}"