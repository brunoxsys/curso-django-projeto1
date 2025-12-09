from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('UMA HOME PAGE :)')

def sobre(request):
    return HttpResponse('PÁGINA SOBRE :)')
