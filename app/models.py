from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    book_count = models.IntegerField(default=0)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

    class Meta:
        ordering = ['-publication_date']
        verbose_name_plural = 'Books'
        verbose_name = 'Book'

    def __str__(self):
        return self.title
