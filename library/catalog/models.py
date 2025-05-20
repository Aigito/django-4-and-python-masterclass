from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length = 150)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length = 150)
  # author is its own model rather than just a simple field

  # on_delete = models.SET_NULL option means that when an author is deleted
  # any book instance with this author will have author set to NULL
  author = models.ForeignKey('Author', on_delete = models.SET_NULL)
  summary = models.TextField(max_length = 600)
  isbn = models.CharField("'ISBN", max_length = 13, unique = True)
  genre = models.ManyToManyField(Genre)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
      return reverse("book_detail", kwargs={"pk": self.pk})


class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  date_of_birth = models.DateField(null = True, blank = True)

  class Meta:
    ordering = ['last_name', 'first_name']

  def get_absolute_url(self):
      return reverse("author_detail", kwargs={"pk": self.pk})

  def __str__(self):
    return f"{self.last_name}, {self.first_name}"

