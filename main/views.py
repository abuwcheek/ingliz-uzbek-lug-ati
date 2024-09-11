from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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

          contact.name = contact_data.get('name')
          contact.number = contact_data.get('number')
          contact.email = contact_data.get('email')
          contact.message = contact_data.get('message')

          contact.save()

          messages.success(request, 'Sizning malumotlaringiz yuborildi')
          return render(request, 'contact.html')



class SearchView(View):
     def get(self, request):
          query = request.GET.get('search')
          if not query:
               return redirect('index')
          search_word = Word.objects.all().filter(Q(en_form__icontains = query) | Q(uz_form__icontains = query) | Q(en_definition__icontains = query) | Q(uz_definition__icontains = query))
          if not search_word:
               messages.warning(request, "So'rov bo'yicha ma'lumot topilmadi")
               return redirect('index')
          
          context = {
               'search_word': search_word,
          }
          messages.info(request, "Siz izlagan ma'lumotlar")
          return render(request, 'search.html', context)