from django.contrib import admin
from .models import Word

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
     list_display = ('en_form', 'uz_form','is_active',)
     list_display_links = ('en_form', 'uz_form',)
     search_fields = ('en_form',)
     prepopulated_fields = {"slug": ('en_form',)}
     readonly_fields = ('id',)
     list_editable = ('is_active',)
     list_per_page = 25