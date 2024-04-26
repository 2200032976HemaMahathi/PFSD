from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")

def login(request):
    return render(request, "login.html")

def About(request):
    return render(request, "About.html")


def Contact(request):
    return render(request, "Contact.html")

def registrationPage(request):
    return render(request, "register.html")

def adminhome(request):
    return render(request, "adminhome.html")