from django.shortcuts import get_object_or_404, render
from .models import Book
from django.http import Http404
from django.db.models import Avg
# Create your views here.


def index(request):
    all_books = Book.objects.all().order_by("rating")  # you can put -
    nofbooks = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))  # rating__avg, rating__min

    return render(request, "book_outlet/index.html", {
        "books": all_books,
        "total_number_of_books": nofbooks,
        "average_rating": avg_rating,
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })
