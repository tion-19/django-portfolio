from django.shortcuts import render, get_object_or_404
from .models import Blogs
# Create your views here.


def home(request):
    blogs = Blogs.objects.order_by('-data')[:3]
    return render(request, 'blog/home.html', {'Blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request, 'blog/detail.html', {'Blog': blog})
