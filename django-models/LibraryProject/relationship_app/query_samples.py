

from .models import Author, Book, Library, Librarian


specific_author = Author.objects.get(name='Author Name')
books_by_author = Book.objects.filter(author=specific_author)
print("Books by Author:", books_by_author)

specific_library = Library.objects.get(name='library Name')
books_in_library = specific_library.books.all()
print("Books in Library:", books_in_library)

specific_library = Library.objects.get(name='Library Name')
librarian = specific_library.librarian
print("Librarian for the Library:", librarian)