from django.contrib import admin
from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'created_time')

admin.site.register(Word, WordAdmin)
