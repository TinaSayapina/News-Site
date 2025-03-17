from django.urls import path
from . import views
from .views import home_page, Register

urlpatterns = [
    path('', home_page),
    path('register', Register.as_view()),

]