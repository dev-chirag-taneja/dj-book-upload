from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .models import Book
from .forms import BookForm

# Create your views here.

# Upload View (used for learning purpose)
def upload(request):
    context= {}
    if request.method == "POST":
        file = request.FILES["document"]
        # print(file.name, file.size)
        fs = FileSystemStorage()
        name = fs.save(file.name, file)
        context = {"url":fs.url(name)}
    return render(request, "upload.html", context)


# List Books
def list_book(request):
    books = Book.objects.all()
    context = {"books":books} 
    return render(request, "list-book.html", context)


# Upload Books
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = BookForm()
    return render(request, 'upload-book.html', {'form': form})


# Delete Books
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        print(book)
        book.delete()
    return redirect('list_book')