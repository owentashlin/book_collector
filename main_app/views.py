# Create your views here.
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .models import Tea

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html') 

def books_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', {'books':books})

def teas_index(request):
  teas = Tea.objects.all()
  return render(request, 'teas/index.html', {'teas':teas})

def books_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  return render(request, 'books/detail.html', {'book':book})

class BookCreate(CreateView):
  model = Book
  fields = '__all__'
  success_url= '/books/'

class BookUpdate(UpdateView):
  model = Book
  fields = ['description', 'rating']
  success_url= '/books/'

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'

def teas_detail(request, tea_id):
  tea = Tea.objects.get(id=tea_id)
  return render(request, 'teas/detail.html', {'tea':tea})

class TeaCreate(CreateView):
  model = Tea
  fields = '__all__'
  success_url= '/teas/'

class TeaUpdate(UpdateView):
  model = Tea
  fields = '__all__'
  success_url= '/teas/'

class TeaDelete(DeleteView):
  model = Tea
  success_url = '/teas/'  
