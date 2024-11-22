from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=20)
    library = models.OneToOneField(Library, on_delete= models.CASCADE)