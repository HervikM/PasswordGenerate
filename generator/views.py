from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, "generator/home.html")


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    isUppercase = request.GET.get('uppercase')
    isNumbers = request.GET.get('numbers')
    isSpecial = request.GET.get('special')

    if isUppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if isNumbers:
        characters.extend(list('1234567890'))

    if isSpecial:
        characters.extend(list('*+-/@_?![{()}];:|°^&$#"%¡'))

    length_password = int(request.GET.get('length'))

    for x in range(length_password):
        generated_password += random.choice(characters)



    return render(request, "generator/password.html", {'password': generated_password, })