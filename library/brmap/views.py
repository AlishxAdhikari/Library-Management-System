from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def home(request):
    return render(request, "home.html")  # Render home.html

@login_required
def addBookView(request):
    return render(request, "addbook.html")

@login_required
def addBook(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        author = request.POST.get("author")
        received_date = request.POST.get("received_date")
        return_date = request.POST.get("return_date")

        if not title or not price or not author:
            messages.error(request, "Title, price, and author are required")
            return render(request, "addbook.html")

        try:
            price = float(price)
        except (TypeError, ValueError):
            messages.error(request, "Price must be a number")
            return render(request, "addbook.html")

        book = Book(
            title=title,
            price=price,
            author=author,
            received_date=received_date or None,
            return_date=return_date or None
        )
        book.save()
        messages.success(request, "Book added successfully")
        return redirect('view-book')

@login_required
def edit_book(request):
    if request.method == "GET":
        book_id = request.GET.get('id')
        if not book_id:
            messages.error(request, "Book ID not provided")
            return redirect('view-book')
        try:
            book = get_object_or_404(Book, id=book_id)
            return render(request, "edit-book.html", {"book": book})
        except ValueError:
            messages.error(request, "Invalid Book ID")
            return redirect('view-book')

    elif request.method == "POST":
        book_id = request.POST.get('bid')
        if not book_id:
            messages.error(request, "Book ID not provided")
            return redirect('view-book')
        try:
            book = get_object_or_404(Book, id=book_id)
            title = request.POST.get("title")
            price = request.POST.get("price")
            author = request.POST.get("author")
            received_date = request.POST.get("received_date")
            return_date = request.POST.get("return_date")

            if not title or not price or not author:
                messages.error(request, "Title, price, and author are required")
                return render(request, "edit-book.html", {"book": book})

            try:
                price = float(price)
            except (TypeError, ValueError):
                messages.error(request, "Price must be a number")
                return render(request, "edit-book.html", {"book": book})

            book.title = title
            book.author = author
            book.price = price
            book.received_date = received_date or None
            book.return_date = return_date or None
            book.save()
            messages.success(request, "Book updated successfully")
            return redirect('view-book')
        except ValueError:
            messages.error(request, "Invalid Book ID")
            return redirect('view-book')

    return redirect('view-book')
@login_required
def deleteBook(request):
    book_id = request.GET.get('id')
    if not book_id:
        messages.error(request, "Book ID not provided")
        return redirect('view-book')
    try:
        book = get_object_or_404(Book, id=book_id)
        if request.method == "POST":
            book.delete()
            messages.success(request, "Book deleted successfully")
            return redirect('view-book')
        return render(request, "delete-book.html", {"book": book})
    except ValueError:
        messages.error(request, "Invalid Book ID")
        return redirect('view-book')

def aboutView(request):
    return render(request, 'about.html')

def helpview(request):
    return render(request, 'help.html')

def contactView(request):
    return render(request, 'contact.html')
    
def baseveiw(request):
    return render(request,'base.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        messages.success(request, "User registered successfully")
        return redirect('login')

    return render(request, 'register.html')



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view-book')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect('login')

def viewBook(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'viewbook.html', {'books': books})