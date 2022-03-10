from django.shortcuts import render


# Create your views here.
def django_doc(request):
    return render(request, 'book/django_set_doc.html')
