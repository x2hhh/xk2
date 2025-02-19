from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

class Member(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    library = models.ForeignKey("Library", on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.DateField()
    library = models.ForeignKey("Library", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

class Request(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Fine(models.Model):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    reason = models.CharField(max_length=200)
    date_issued = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)