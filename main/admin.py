from django.contrib import admin
from .models import Category, Word


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