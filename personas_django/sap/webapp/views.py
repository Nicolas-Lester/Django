from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    email = 'nicolasherreramontes625@gmail.com'
    telefono = '+56964484168'
    return HttpResponse([f'Email: {email}'
                         '\n'
                         f'Telefono: {telefono}'])