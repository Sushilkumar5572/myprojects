from django.db import models
from django.urls import reverse
from django.shortcuts import render

# Create your models here.

class Contact(models.Model):
    """Model class for storing and accessing contact from database."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse("edit-contact", kwargs={"id": self.id})
