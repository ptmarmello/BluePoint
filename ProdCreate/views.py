# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render,redirect, get_object_or_404, reverse

#,render_to_response
from django.core import serializers
from .models import Usuario, Seguradora, Product
# Create your views here.
from django.http import HttpResponse,Http404
from .forms import ProductForm, UsuarioForm, UpdateSaldo
import json

def home(request):
    user = Usuario.objects.get(id=1)
    seg = Seguradora.objects.all()
    prods = Product.objects.all()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prods = form.save()
            return redirect(reverse('templatepage'),{'produtos':prods,'seguradora':seg, 'user':user,'form':form})
    else:
        form = ProductForm()
    return render(request,'index.html',{'produtos':prods,'seguradora':seg, 'user':user,'form':form})
    
def radial(request):
    prodcts=Product.objects.all()
    
    return render(request, 'TesteMaps.html', {'prods': prodcts})


def walletpage(request,name):
    user = Usuario.objects.get(name=name)
    prods= user.products.all()

    return render(request, 'wallet.html',{'produtos':prods,'user':user})

def listpage(request):
    prods = Product.objects.all()
    user = Usuario.objects.get(id=1)
   
    
    return render(request, 'list.html',{'produtos':prods,'user':user})

def configpage(request,name):
    user=Usuario.objects.get(name=name)

    return render(request, 'settings.html',{'user':user})


def productpage(request,pk):
    prods = Product.objects.get(pk=pk)
    user = Usuario.objects.get(id=1)
    
    return render(request, 'product.html',{'produtos':prods,'user':user})


def adminpage(request):
    user = Usuario.objects.all()
    seg = Seguradora.objects.first()
    prods = Product.objects.all()
    
    return render(request,'AdminPage.html',{'produtos':prods,'seguradora':seg,'user':user})    


def formpage(request):
    seg=Seguradora.objects.first()
    prods=Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prods = form.save()
            return redirect(reverse('adminpage'),{'produtos':prods,'seguradora':seg,'form':form})
    else:
        form = ProductForm()
    return render(request, 'Form Page.html',{'produtos':prods,'form':form,'seguradora':seg})


def segloginpage(request):

    return render(request,'login.html')

def userlogin(request):
    user = Usuario.objects.get(id=1)
    

    return render (request, 'userlogin.html',{'user':user})


def testes(request):
    prods=Product.objects.all()
    user=Usuario.objects.all()
    

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            prods = form.save()
            return redirect(reverse('home'),{'prods':prods,'form':form,'user':user})
    else:
        form = ProductForm()
    return render(request, 'TesteDoForms.html',{'prods':prods,'form':form,'user':user})

def onboarding(request):

    return render(request, 'Onboarding.html')

def quizpage(request):

    return render(request, 'quiz1.html')

def quizpage_2(request):

    return render(request, 'quiz2.html')
def quizpage_3(request):

    return render(request, 'quiz3.html')
def quizpage_4(request):

    return render(request, 'quiz4.html')

def quizpage_5(request):

    return render(request, 'quiz5.html')


