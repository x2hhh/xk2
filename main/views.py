
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.shortcuts import get_object_or_404
from .models import Library, Member, Category, Book, Request, Review, Fine

from .import models
def print_hello(request):
    return render(request,
                  'index.html',
                  context={
                      'sendings': Book.objects.all() 
                  })

def index(request):
    return render(request, {'question': models.Qustion.objects.all()})
# class QuestionListView(ListView):
#     model = models.Qustion
#     temlate_name = 'index.html'
#     Context_objext_name = 'questions'


class LibraryistView(ListView):
    model = models.Library
    template_name = 'Library.html'
    context_object_name = 'Library'


class MemberListView(ListView):
    model = models.Member
    template_name = 'member.html'
    context_object_name = 'member'


class CategoryView(ListView):
    model = models.Category
    template_name = 'category.html'
    context_object_name = 'category'


class BookView(ListView):
    model = models.Book
    template_name = 'book.html'
    context_object_name = 'book'


class RequestView(ListView):
    model = models.Request
    template_name = 'request.html'
    context_object_name = 'request'


class ReviewView(ListView):
    model = models.Review
    template_name = 'review.html'
    context_object_name = 'review'


class FineView(ListView):
    model = models.Fine
    template_name = 'fine.html'
    context_object_name = 'fine'





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})


def library_list(request):
    libraries = Library.objects.all()
    return render(request, 'library/library_list.html', {'libraries': libraries})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members': members})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'library/category_list.html', {'categories': categories})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'library/request_list.html', {'requests': requests})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'library/review_list.html', {'reviews': reviews})

def fine_list(request):
    fines = Fine.objects.all()
    return render(request, 'library/fine_list.html', {'fines': fines})

def profile(request):
    return render(request, 'registration/profile.html')