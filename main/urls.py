from django.urls import path
from .views import CategoryView, CategoryDetailView, WordView, DetailView, AboutView, ContactView, SearchView


urlpatterns=[
     path('category/', CategoryView.as_view(), name="categ"),     
     path('category/<str:slug>/', CategoryDetailView.as_view(), name="ctgdetail"),     
     path('', WordView.as_view(), name="index"),     
     path('word/<str:slug>', DetailView.as_view(), name="detail"), 
     path('about/', AboutView.as_view(), name="abouturl"),     
     path('contact/', ContactView.as_view(), name="contacturl"),     
     path('search/', SearchView.as_view(), name="search"),     
]