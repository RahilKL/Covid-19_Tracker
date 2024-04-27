from django.shortcuts import render


def Base(request):
    return render(request, "Base.html")


def Login(request):
    return render(request, "Login.html")


def Signup(request):
    return render(request, "Signup.html")


def logout(request):
    return render(request, "Base.html")


def Services(request):
    return render(request, "Services.html")
