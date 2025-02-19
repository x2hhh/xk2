from . import views
from django.urls import path
from .views import register, home
from django.contrib.auth import views as auth_views
from .views import (
    register, 
    home, 
    library_list, 
    member_list, 
    category_list, 
    book_list, 
    request_list, 
    review_list, 
    fine_list,
    profile
)
urlpatterns = [
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('libraries/', library_list, name='library_list'),
    path('members/', member_list, name='member_list'),
    path('categories/', category_list, name='category_list'),
    path('books/', book_list, name='book_list'),
    path('requests/', request_list, name='request_list'),
    path('reviews/', review_list, name='review_list'),
    path('fines/', fine_list, name='fine_list'),
]