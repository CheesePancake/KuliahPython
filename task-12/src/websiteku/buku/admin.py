from django.contrib import admin
from . models import Post, Kategori
# Register your models here.

class TampilBuku(admin.ModelAdmin):
    list_display = ('judul', 'kategori')
    list_display_links = (None)

admin.site.register(Post, TampilBuku)
admin.site.register(Kategori)