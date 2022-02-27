from django.contrib import admin

import authApp
from .models import Author, Book


admin.site.register(Author)
admin.site.register(Book)