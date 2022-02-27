from operator import truediv
from pickle import TRUE
from pyexpat import model
from random import choice
from statistics import mode
from django.db import models


class Author(models.Model):

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )

    name = models.CharField(max_length=120, unique=True)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=120, choices=gender_choices, default='Male')
    country = models.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.name)

    
class Book(models.Model):

    name = models.CharField(max_length=120, unique=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=TRUE)
    date_publishing = models.DateField()
    number_of_pages = models.CharField(max_length=10)
    avg_critics_rating = models.CharField(max_length=2)

    def __str__(self):
        return '{}-{}'.format(self.name, self.author.name)

        
