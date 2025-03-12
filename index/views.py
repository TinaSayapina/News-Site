from django.shortcuts import render
from django.http import HttpResponse
from .models import News, NewsCategory

def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {
        'categories':categories,
        'news':news
    }
    return render(request,'home.html',context)