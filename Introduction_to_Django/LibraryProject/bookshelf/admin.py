from django.contrib import admin
from .models import Book
admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    # Specify the fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable filtering by author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for title and author
    search_fields = ('title', 'author__name')  # Assuming author is a ForeignKey with a 'name' field