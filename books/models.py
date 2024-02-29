from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Books(models.Model):

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):

        return self.title

    def __repr__(self):

        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])
