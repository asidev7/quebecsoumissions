from django.shortcuts import render

from base.models import Blog, Service, Type_Soumission

# Create your views here.
def home(request):
    categories = Service.objects.all()
    blogs = Blog.objects.all()
    chunked_blogs = [blogs[i:i + 3] for i in range(0, len(blogs), 3)]

    params ={
        'categories':categories,
        'blogs':blogs,
        'chunked_blogs':chunked_blogs
    }
    return render(request,'main/index.html',params)


def blog(request):
    blogs = Blog.objects.all()
    params ={
        'blogs':blogs
    }
    return render(request,'pages/blog.html',params)


def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    params ={
        'blog':blog
    }
    return render(request,'pages/details_blog.html',params)

def services(request):
    return render(request,'pages/services.html')\
    
def forfaits(request):
    return render(request,'pages/forfaits.html')

def repertoire(request):
    return render(request,'pages/repertoire.html')

def details_soumission(request,id=id):
    soumission = Type_Soumission.objects.get(id=id)
    params ={
        'soumission':soumission
    }
    return render(request,'pages/details-soumission.html',params)

def Soummision(request):
    return render(request,'pages/soumission.html')

def inscription_entrepreneur(request):
    return render(request,'pages/inscription_entrepreneur.html')

def inscription_client(request):
    return render(request,'pages/inscription_client.html')


def contact(request):
    return render(request,'main/contact.html')