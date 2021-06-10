from django.shortcuts import render, redirect
from ba_app.models import Book, Author

def index(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, 'index.html', context)

def book_submit(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
    b = Book.objects.create(title = title, desc = desc)
    b.save()
    return redirect('/')

def book_display(request, book_id):
    book = Book.objects.get(id= book_id)
    non_authors = Author.objects.exclude(books__id = book.id)

    context = {
        'book': book,
        'non_authors': non_authors
    }
    return render(request, 'book_id.html', context)

def book_add(request):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author_id'])

    book.authors.add(author)
    return redirect(f'/books/{book.id}')


def author(request):
    authors = Author.objects.all()

    context = {
        'authors': authors
    }
    return render(request, 'author.html', context)

def author_submit(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        notes = request.POST['notes']
    a = Author.objects.create(first_name = fname, last_name = lname, notes = notes)
    a.save()
    return redirect('/author')

def author_display(request, author_id):
    author = Author.objects.get(id= author_id)
    non_books = Book.objects.exclude(authors__id = author.id)

    context = {
        'author': author,
        'non_books': non_books
    }
    return render(request, 'author_id.html', context)

def author_add(request):
    author = Author.objects.get(id = request.POST['author_id'])
    book = Book.objects.get(id = request.POST['book_id'])

    author.books.add(book)
    return redirect(f'/authors/{author.id}')