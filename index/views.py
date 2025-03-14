from django.shortcuts import render
from django.http import HttpResponse
from .models import News, NewsCategory
import random


def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()

    items = list(News.objects.all())

    # change 3 to how many random items you want
    random_items = random.sample(items, 3)
    # if you want only a single random item
    random_item = random.choice(items)

    context = {
        'categories':categories,
        'news':news,
        'random':random_item
    }
    return render(request,'home.html',context)