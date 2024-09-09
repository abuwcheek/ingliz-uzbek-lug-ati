from django.contrib import admin
from .models import Category, Word, About, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('title', 'created_at', 'is_active')
     list_display_links = ('title', 'created_at')
     search_fields = ('title',)
     # filter_horizontal = ('title', 'created_at')
     prepopulated_fields = {"slug": ('title',)}
     readonly_fields = ('id',)
     list_per_page = 25



@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
     list_display = ('en_form', 'uz_form','is_active',)
     list_display_links = ('en_form', 'uz_form',)
     search_fields = ('en_form',)
     prepopulated_fields = {"slug": ('en_form',)}
     readonly_fields = ('id',)
     list_editable = ('is_active',)
     list_per_page = 25



@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
     list_display = ('created_at', 'is_active')
     list_display_links = ('created_at', 'is_active')



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'email', 'number', 'is_active', 'created_at')
     list_display_links = ('name', 'email')
     search_fields = ('name', 'email')
     list_editable = ('is_active',)
