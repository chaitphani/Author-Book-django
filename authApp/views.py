from email import message
from django.shortcuts import render, redirect
from django.contrib import messages

import os
import csv, io

from .models import Author, Book


def author_create(request):

    if request.method == 'POST':
        author_obj = Author.objects.create(name=request.POST.get('name'), age=request.POST.get('age'), gender=request.POST.get('gender'), country = request.POST.get('country'))

        author_obj.save()
        return redirect('author_list')


def author_list(request):
    author_list = Author.objects.all()
    return render(request, 'authors.html', {'authors':author_list})


def book_create(request):

    if request.method == 'POST':
        author = Author.objects.get(id=request.POST.get('author'))
        book_obj = Book.objects.create(name=request.POST.get('name'), author=author, date_publishing=request.POST.get('date_publishing'), number_of_pages = request.POST.get('number_of_pages'), avg_critics_rating = request.POST.get('avg_critics_rating'))

        book_obj.save()
        return redirect('book_list')


def book_list(request):
    book_list = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'books.html', {'books':book_list, 'authors':authors})



def import_authors(request):

    if request.method == 'POST':
        file = request.FILES.get('authors_csv')
        try:
            data_set = file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            csv_reader = csv.reader(io_string)
            next(csv_reader)

            for values in csv_reader:
                if not Author.objects.filter(name=values[0]).exists():
                    Author.objects.create(name=values[0], age=values[1], gender=values[2], country=values[3])
                else:
                    pass

        except Exception as e:
            messages.error(request, e)
    return redirect('author_list')


from datetime import datetime
def import_books(request):

    if request.method == 'POST':
        file = request.FILES.get('books_csv')
        try:
            data_set = file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            csv_reader = csv.reader(io_string)
            next(csv_reader)

            for values in csv_reader:
                if not Book.objects.filter(name=values[0]).exists():
                    date_time_str = values[2]
                    date_time_obj = datetime.strptime(date_time_str, '%d-%m-%Y')

                    if not Author.objects.filter(name=values[1]).exists():
                        author_obj = Author.objects.filter(name=values[1])
                        Book.objects.create(name=values[0], author=author_obj.last(), date_publishing=date_time_obj, number_of_pages=values[3], avg_critics_rating=values[4])
                else:
                    pass
        except Exception as e:
            messages.error(request, e)
    return redirect('book_list')
