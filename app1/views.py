from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

def index_view(request):
    a = 1
    b = 2
    result = a + b

    return HttpResponse(f'Сумма чисел {result}')


def home_view(request):

    url = reverse('index')
    return HttpResponse(F'Для просмотра расчета перейди по ссылке {url}')
