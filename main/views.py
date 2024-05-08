from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Word


class WordView(View):
     def get(self, request):
          wordcha = Word.objects.all()
          context={
               'wordcha': wordcha,
          }
          return render(request, 'index.html', context)


class DetailView(View):
     def get(self, request, slug):
          data = Word.objects.get(slug=slug)
          context = {
               'data': data,
          }
          return render(request, 'detail.html', context)