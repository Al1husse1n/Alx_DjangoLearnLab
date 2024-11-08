```python
from bookshelf.models import Book
>>> book.delete()
>>> all_books = Book.objects.all()
>>> print(all_books)  # Should show an empty QuerySet if the book was deleted