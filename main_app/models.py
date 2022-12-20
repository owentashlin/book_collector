from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):  
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Reading(models.Model):
    date: models.DateField('start date')
    page: models.IntegerField('page number')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_page_display()} on {self.date}"