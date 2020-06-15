from django.contrib import admin

# Register your models here.

from .models import Newspaper, Word

admin.site.register(Newspaper)
admin.site.register(Word)