from django.shortcuts import render, redirect
from .models import Book, Author

# Books Page
def index(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all(),
    }
    return render(request, 'index.html', context)


# Add book
def add_book(request):
    Book.objects.create(
        title=request.POST['title'], desc=request.POST['description'])
    return redirect('/')


# Show book
def show_book(request, book_id):
    book_in_question = Book.objects.get(id=book_id)
    context = {
        "book": book_in_question,
        "authors_excluded": Author.objects.exclude(books=book_in_question),
    }
    return render(request, 'show_book.html', context)


# Add author to book 
def add_author_to_book(request, book_id):
    book = Book.objects.get(id=book_id)
    author_id = request.POST['author']
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f"/books/{book_id}")


# Authors page
def authors(request):
    context = {
        "all_the_books": Book.objects.all(),
        "all_the_authors": Author.objects.all(),
    }
    return render(request, 'authors.html', context)


# Add author
def add_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')


# Show author
def show_author(request, author_id):
    author_in_question = Author.objects.get(id=author_id)
    context = {
        "author": author_in_question,
        "books_excluded": Book.objects.exclude(authors=author_in_question),
    }

    return render(request, 'show_author.html', context)

# Add book to author
def add_book_to_author(request, author_id):
    book_id = request.POST['books']
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    author.books.add(book)
    return redirect(f"/author/{author.id}")