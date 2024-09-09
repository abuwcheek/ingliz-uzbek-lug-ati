from django.urls import path
from .views import CategoryView, WordView, DetailView


urlpatterns=[
     path('category/', CategoryView.as_view(), name="categ"),     
     path('', WordView.as_view(), name="index"),     
     path('detail/<str:slug>', DetailView.as_view(), name="detail"),     
]