

from .models import Author, Book, Library, Librarian
library_name = 'Library name'
author_name = 'author name'
author = 'author'
specific_author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=specific_author)
books_by_author = Book.objects.filter(author=author)

print("Books by Author:", books_by_author)
 

specific_library = Library.objects.get(name=library_name)
books_in_library = specific_library.books.all()
print("Books in Library:", books_in_library)

specific_library = Library.objects.get(name=library_name)
librarian = specific_library.librarian
print("Librarian for the Library:", librarian)