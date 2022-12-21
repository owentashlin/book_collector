# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .models import Tea
from .forms import ReadingForm

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
  id_list = book.teas.all().values_list('id')
  available_teas = Tea.objects.exclude(id__in=id_list)
  reading_form = ReadingForm()
  return render(request, 'books/detail.html', {'book':book, 'reading_form':reading_form, 'teas':available_teas})

def add_reading(request, book_id):
  form=ReadingForm(request.POST)
  if form.is_valid():
    new_reading=form.save(commit=False)
    new_reading.book_id = book_id
    new_reading.save()
  return redirect('book_detail', book_id = book_id)

def assoc_tea(request, book_id, tea_id):
  Book.objects.get(id=book_id).teas.add(tea_id)
  return redirect('book_detail', book_id=book_id)

class BookCreate(CreateView):
  model = Book
  fields = ['title', 'author', 'description', 'rating']
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
