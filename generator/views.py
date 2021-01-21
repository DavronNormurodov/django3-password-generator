from django.shortcuts import render
from django.http import HttpResponse
from random import choice
# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': "jdgcv2udh3bndiu"})

def password(request):

    length = int(request.GET.get('length', '12'))
    characters = list('abcdefghijklmnopqrstvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXWZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    thepassword = ''
    for i in range(length):
        thepassword += choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    
    return render(request, 'generator/about.html')