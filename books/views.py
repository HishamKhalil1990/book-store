from django.db import models
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from .models import Book, Auther
from django.urls import reverse_lazy

# Create your views here.
class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = Book

class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    model = Book
    def get_context_data(self, *args, **kwargs):
        context = super(BookDetailView, self).get_context_data(*args, **kwargs)
        context['auther'] = Auther.objects.all()
        return context

class BookCreateView(CreateView):
    template_name = 'books/book_create.html'
    model = Book
    fields = ['title','auther', 'category','isbn','description','employee',]

class BookUpdateView(UpdateView):
    template_name = 'books/book_update.html'
    model = Book
    fields = ['title','auther', 'category','isbn','description','employee',]

class BookDeleteView(DeleteView):
    template_name = 'books/book_delete.html'
    model = Book
    success_url = reverse_lazy('book_list')