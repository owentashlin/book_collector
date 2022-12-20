from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):  
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Reading(models.Model):
    date: models.DateField()
    page: models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)