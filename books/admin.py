from django.contrib import admin
from .models import *

class BookCopyInline(admin.TabularInline):
    model = BookCopy
    extra = 1

class LibraryAdmin(admin.ModelAdmin):
    inlines = [BookCopyInline]
    list_display = ['name']

class BookAdmin(admin.ModelAdmin):
    inlines = [BookCopyInline]
    list_display = ['title', 'author']

admin.site.site_header = 'Kamu administration'
admin.site.site_title = 'Kamu administration'
admin.site.index_title = None
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)