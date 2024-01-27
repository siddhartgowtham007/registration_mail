from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def registration(request):
    ufo=userforms()
    pfo=profileforms()
    d={'ufo':ufo,'pfo':pfo}

    if request.method=='POST' and request.FILES:
        ufd=userforms(request.POST)
        pfd=profileforms(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUSFO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUSFO.set_password(pw)
            MUSFO.save()

            MPUFO=pfd.save(commit=False)
            MPUFO.username=MUSFO
            MPUFO.save()
            send_mail('registration','thank u for registration','siddharthgowtham1432@gmail.com',
                      [MUSFO.email],fail_silently=False,)
            
            return HttpResponse('registration successful')
        else:
            return HttpResponse('invalid credentials')

    return render(request,'registration.html',d)