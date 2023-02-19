from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


class BookListView(generic.ListView):
    model = Book


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_availabel = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    return render(request, 'index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_availabel': num_instances_availabel,
                                                  'num_authors': num_authors,
                                                  })
