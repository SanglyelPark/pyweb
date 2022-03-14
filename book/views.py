from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def django_doc(request):
    return render(request, 'book/django_set_doc.html')


def about_me(request):
    return render(request, 'book/about_me.html')
