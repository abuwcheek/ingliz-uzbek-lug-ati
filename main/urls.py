from django.urls import path
from .views import WordView, DetailView


urlpatterns=[
     path('', WordView.as_view(), name="index"),     
     path('detail/<str:slug>', DetailView.as_view(), name="detail"),     
]