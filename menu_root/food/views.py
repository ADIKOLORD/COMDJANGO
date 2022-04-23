from django.shortcuts import render, HttpResponse


def first_page(request):
    return HttpResponse('<h1>ADILET</h1>')


def main_page(request):
    return render(request, 'index.html')



