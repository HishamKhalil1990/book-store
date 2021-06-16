from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Auther(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    nationality = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=256)
    auther = models.ForeignKey(Auther,on_delete=models.CASCADE)
    category = models.CharField(max_length=256)
    isbn = models.IntegerField()
    description = models.TextField()
    employee = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail',args=[str(self.id)])
