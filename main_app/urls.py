from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('books/', views.books_index, name='index'),

    path('teas/', views.teas_index, name='index'),

    path('books/<int:book_id>', views.books_detail, name='book_detail'),

    path('teas/<int:tea_id>', views.teas_detail, name='tea_detail'),

    path('books/create/', views.BookCreate.as_view(), name='books_create'),

    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),

    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),

    path('teas/create/', views.TeaCreate.as_view(), name='teas_create'),

    path('teas/<int:pk>/update/', views.TeaUpdate.as_view(), name='teas_update'),

    path('teas/<int:pk>/delete/', views.TeaDelete.as_view(), name='teas_delete'),
]