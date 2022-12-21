# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .models import Tea
from .forms import ReadingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html') 

@login_required
def books_index(request):
  books = Book.objects.filter(user=request.user)
  return render(request, 'books/index.html', {'books':books})

@login_required
def teas_index(request):
  teas = Tea.objects.all()
  return render(request, 'teas/index.html', {'teas':teas})

@login_required
def books_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  id_list = book.teas.all().values_list('id')
  available_teas = Tea.objects.exclude(id__in=id_list)
  reading_form = ReadingForm()
  return render(request, 'books/detail.html', {'book':book, 'reading_form':reading_form, 'teas':available_teas})

@login_required
def add_reading(request, book_id):
  form=ReadingForm(request.POST)
  if form.is_valid():
    new_reading=form.save(commit=False)
    new_reading.book_id = book_id
    new_reading.save()
  return redirect('book_detail', book_id = book_id)

@login_required
def assoc_tea(request, book_id, tea_id):
  Book.objects.get(id=book_id).teas.add(tea_id)
  return redirect('book_detail', book_id=book_id)

@login_required
def remove_tea(request, book_id, tea_id):
  Book.objects.get(id=book_id).teas.remove(tea_id)
  return redirect('book_detail', book_id=book_id)

class BookCreate(LoginRequiredMixin, CreateView):
  model = Book
  fields = ['title', 'author', 'description', 'rating']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
  model = Book
  fields = ['description', 'rating']
  success_url= '/books/'

class BookDelete(LoginRequiredMixin, DeleteView):
  model = Book
  success_url = '/books/'

@login_required
def teas_detail(request, tea_id):
  tea = Tea.objects.get(id=tea_id)
  return render(request, 'teas/detail.html', {'tea':tea})

class TeaCreate(LoginRequiredMixin, CreateView):
  model = Tea
  fields = '__all__'
  success_url= '/teas/'

class TeaUpdate(LoginRequiredMixin, UpdateView):
  model = Tea
  fields = '__all__'
  success_url= '/teas/'

class TeaDelete(LoginRequiredMixin, DeleteView):
  model = Tea
  success_url = '/teas/'  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)