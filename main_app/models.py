from django.db import models
from django.urls import reverse

class Tea(models.Model):  
    brand = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()
    objects = models.Manager()
    
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('tea_detail', kwargs={'tea_id': self.id})

class Book(models.Model):  
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    rating = models.IntegerField()
    teas = models.ManyToManyField(Tea)
    
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'book_id': self.id})

class Reading(models.Model):
    date = models.DateField('reading date')
    page = models.CharField(max_length=10)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.page} on {self.date}")

    class Meta:
        ordering = ['-date']