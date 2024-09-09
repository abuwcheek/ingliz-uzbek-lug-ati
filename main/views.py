from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .models import Category, Word, About, Contact


class CategoryView(View):
     def get(self, request):
          category = Category.objects.all().filter(is_active=True)
          context = {
               'category': category,
          }
          return render(request, 'category_list.html', context)



class CategoryDetailView(View):
     def get(self, request, slug):
          categ_detail = get_object_or_404(Category, slug=slug)
          categ_word = categ_detail.category_word.all()

          context = {
               'categ_word': categ_word,
          }
          return render(request, 'category_detail.html', context)



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



class AboutView(View):
     def get(self, request):
          about_view = About.objects.all()
          context = {
               'about_view': about_view,
          }
          return render(request, 'about.html', context)


class ContactView(View):
     def get(self, request):
          return render(request, 'contact.html')

     def post(self, request):
          contact_data = request.POST
          contact = Contact()
          contact.name = data.get('name')
          contact.number = data.get('number')
          contact.email = data.get('email')
          contact.name = data.get('message')
          contact.save()

          messages.success(request, 'Sizning malumotlaringiz yuborildi')
          return render(request, 'contact.html')
