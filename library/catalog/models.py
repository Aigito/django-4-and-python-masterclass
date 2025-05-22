from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length = 150)

  def __str__(self):
    return self.name

class Language(models.Model):
  name = models.CharField(max_length = 50)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length = 150)
  # author is its own model rather than just a simple field

  # on_delete = models.SET_NULL option means that when an author is deleted
  # any book instance with this author will have author set to NULL
  author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
  summary = models.TextField(max_length = 600)
  isbn = models.CharField("'ISBN", max_length = 13, unique = True)
  genre = models.ManyToManyField(Genre)
  language = models.ForeignKey('Language', on_delete = models.SET_NULL, null = True)

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

# BookInstance represent copies of a single book
# i.e. A library can have multiple copies of the same book
# This is done to maintain:
# - separation of concepts
# - efficient data storage (no storing the same ISBN 50 times)
# - individual copy tracking
# - better instance management
# - scalability
# - consistency and data integrity (single source of truth)
class BookInstance(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4)

  # RESTRICT prevents Book model instance to be deleted when there is a connected BookInstance
  book = models.ForeignKey('Book', on_delete = models.RESTRICT, null = True)
  imprint = models.CharField(max_length = 50)
  due_back = models.DateField(null = True, blank = True)
  borrower = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

  LOAN_STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On Loan'),
    ('a', 'Available'),
    ('r', 'Reserved'),
  )

  status = models.CharField(
    max_length=1,
    choices = LOAN_STATUS,
    blank = True,
    default = 'm'
  )

  class Meta:
    ordering = ['due_back']

  def __str__(self):
    return f'{self.id} ({self.book.title})'