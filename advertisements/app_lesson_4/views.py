from django.http import HttpResponse


def index(request):
    return HttpResponse(" Домашка по 4 занятию")


from django.shortcuts import render

# Create your views here.
