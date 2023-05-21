from django.shortcuts import render
from . models import Post
 
def index(request):
     # QuerySet
     postingan = Post.objects.all()
     
     context = {
         'TampungPostingan': postingan
     }
     
     return render(request, 'buku/index.html', context)

