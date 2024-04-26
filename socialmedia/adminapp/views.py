from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Admin, Register, Packages, Post


def ttmhome(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Create a new post with the authenticated user instance
            Post.objects.create(title=title, content=content, user=request.user)
            messages.success(request, "Post created successfully.")
            return HttpResponseRedirect(request.path)  # Redirect back to the same page after posting
        else:
            messages.error(request, "User is not authenticated.")
            return HttpResponseRedirect(request.path)  # Redirect back to the same page
    else:
        # Retrieve already posted posts
        posts = Post.objects.all()
        return render(request, "ttmhome.html", {"posts": posts})

def loginfail(request):
    return render(request, "loginfail.html")


def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST.get("uname")
        password = request.POST.get("pwd")

        # Check if the user exists and the password is correct
        user = Register.objects.filter(username=name, password=password).first()
        if user:
            if name == "adminname":  # Replace "adminname" with your admin username
                messages.info(request, "Welcome, admin!")
                # Retrieve existing posts
                posts = Post.objects.all()
                return render(request, "adminhome.html", {"posts": posts})  # Display admin dashboard with posts
            else:
                messages.info(request, "This is user's TTM page")
                return redirect("ttmhome")  # Redirect to user dashboard

        else:
            messages.error(request, "Invalid Credentials!!")
            return render(request, "loginfail.html")

    # If method is not POST, render login page
    return render(request, "login.html")

def checkregistration(request):
    if request.method  == "POST":
         name = request.POST["name"]
         addr = request.POST["addr"]
         email = request.POST["email"]
         phno = request.POST["phno"]
         uname = request.POST["uname"]
         pwd = request.POST["pwd"]
         cpwd = request.POST["cpwd"]
         if pwd==cpwd:
             if Register.objects.filter(username=uname).exists():
                 messages.info(request,"username existing..!!")
                 return render(request,"register.html")
             elif Register.objects.filter(email=email).exists():
                 messages.info(request,"email existing..!!")
                 return render(request,"register.html")
             else:
                 user=Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                 user.save()
                 messages.info(request,"user created")
                 return render(request,"login.html")
         else:
             messages.info(request,"password not matching..!!")
             return render(request,"register.html")

def checkpackages(request):
    if request.method == "POST":
        acode = request.POST["accountcode"]
        aname = request.POST["accounttitle"]
        apack = request.POST["accountpackage"]
        adesc = request.POST["desc"]
        pack= Packages.objects.create(tourcode=acode,tourname=aname,tourpackage=apack,desc=adesc)
        pack.save()
        messages.info(request,"Data Inserted Sucessfully🥳")
        return render(request,"package.html")
    else:
        return render(request, "package.html")
def viewplaces(request):
    data = Packages.objects.all()
    return render(request,"viewplaces.html",{"placesdata":data})


def checkChangePassword(request):
    if request.method=="POST":
        uname=request.POST["uname"]
        opwd=request.POST["opwd"]
        npwd=request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            messages.info(request, "Password Updated")
            return render(request,"index.html")
        else:
            return render(request,"index.html")
    else:
        return render(request,"changepassword.html")

def contact(request):
    return render(request,'mail.html')
def logout(request):
    messages.info(request,"logout")
    return render(request,"index.html")