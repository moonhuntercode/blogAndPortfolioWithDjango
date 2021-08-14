from blogs.models import BlogPost
from django.shortcuts import render

# Create your views here.
def blog(request,id):
    blog=BlogPost.objects.get(id=id)
    return render(request,"blog/blog.html",{'blog':blog})
def home(request):
    blogsito=BlogPost.objects.all()
    return render(request,"blog/home.html",{'blogList':blogsito})