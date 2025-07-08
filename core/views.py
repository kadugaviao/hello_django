from django.shortcuts import render, HttpResponse

def hello(request, nome, idade):
    return HttpResponse(f'<h1> Hello {nome} de {idade} anos.</h1>')

def soma(request, num1, num2):
    return HttpResponse (f'<h1> {num1} + {num2} = {num1 + num2}</h1>')

def subtrai(request, num1, num2):
    return HttpResponse (f'<h1>{num1} - {num2} = {num1 - num2} </h1>')

def divide(request, num1, num2):
    return HttpResponse (f'<h1>{num1} / {num2} = {num1 / num2}</h1>')

def multiplica(request, num1, num2): 
    return HttpResponse (f'<h1>{num1} * {num2} = {num1 * num2}</h1>')

