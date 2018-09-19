from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    notes = models.TextField()

    def __str__(self):
        return self.first_name