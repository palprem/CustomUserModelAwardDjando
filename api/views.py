from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import date
today = date.today()

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass']
        print("username>>",username)
        print("username>>",password)
        # user=auth.authenticate(username=username)
        user=Account.objects.get(username=username)
        if user is not None:
            auth.login(request, user)
            return render(request,'award.html')
        return render(request, 'login.html',{'error':'invalid login cradintal'})
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        passwordagain=request.POST['passwordagain']
        first_name=request.POST['first_name']
        email=request.POST['email']
        phone=request.POST['phone']
        location=request.POST['location']
        picture=request.POST['picture']
        if password==passwordagain:
            try:
                user= Account.objects.get(username=username,password=password)
                return render(request, 'register.html',{'error':'username has already been taken'})
            except :
                user=Account.objects.create_user(username=username,
                                                password=password,
                                                first_name=first_name,
                                                email=email,
                                                phone=phone,
                                                location=location,
                                                picture=picture)
                auth.login(request, user)
                return render(request, 'login.html', {'msg':'Registration complited!'})

        return render(request, 'register.html', {'msg':'password don`t match'})

    return render(request, 'register.html')

@login_required(login_url='/login/')
def award(request):
    if request.method=='POST':
        title=request.POST['title']
        try:
            title=Award.objects.get(title=title)
            return render(request, 'award.html',{'msg':'This Title Already Present in Data Base'})
        except:
            point=request.POST['point']
            user= Account.objects.get(username=request.user)
            # print(user.picture)
            img=user.picture
            AllData=Award(acconut_id=user,
                        title=title,
                        point=point
                        )
            AllData.save()
            data=Award.objects.filter(acconut_id=user)
            # img = Account.objects.filter(picture='image')
            # print(data)
            return render(request, 'award.html', {'error':'Data saved!','datas':data, 'user':user,'img':img})
    # data=Award.objects.filter(acconut_id=user)
    return render(request, 'award.html',{'datas':data})
