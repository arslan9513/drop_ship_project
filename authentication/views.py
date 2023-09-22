from django.shortcuts import render


def login(request):
    return render(request, 'authenticatin/login.html',)


# Create your views here.
