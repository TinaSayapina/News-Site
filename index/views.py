from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, NewsCategory
import random
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegForm
from django.views import View


def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()

    items = list(News.objects.all())

    # change 3 to how many random items you want
    random_items = random.sample(items, 1)
    # if you want only a single random item
    random_item = random.choice(items)

    context = {
        'categories':categories,
        'news':news,
        'random':random_item
    }
    return render(request,'home.html',context)

class Register(View):

    def get(self,request):
        template = 'registration/signup.html'
        return render(request,template,{'form':RegForm})

    def post(self,request):
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username = username,
                                     email = email,
                                     password=password)
            user.save()

            login(request, user)
            return redirect('/')





