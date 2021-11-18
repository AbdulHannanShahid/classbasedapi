from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
  
   path('apicheck/', views.getpost.as_view()),
   path('apicheck/<int:id>', views.delput.as_view()),
   
]