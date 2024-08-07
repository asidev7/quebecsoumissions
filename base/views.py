from django.shortcuts import redirect, render

from base.forms import SoumissionForm
from base.models import Blog, Realisation, Service, Type_Soumission
from .forms import ClientForm, UserForm, EntrepriseForm
from django.contrib.auth.models import User
from .forms import UserForm


# Create your views here.
def home(request):
    categories = Service.objects.all()
    blogs = Blog.objects.all()
    chunked_blogs = [blogs[i:i + 3] for i in range(0, len(blogs), 3)]
    realisations = Realisation.objects.all()

    params ={
        'categories':categories,
        'blogs':blogs,
        'realisations':realisations,
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
    if request.method == 'POST':
        form = SoumissionForm(request.POST)
        if form.is_valid():
            soumission = form.save(commit=False)
            soumission.user = request.user  # Assurez-vous que l'utilisateur est connecté
            soumission.save()
            return redirect(home)  # Redirigez vers une page de succès appropriée
    else:
        form = SoumissionForm()

    params ={
        'form':form,
        'soumission':soumission
    }
    return render(request,'pages/details-soumission.html',params)

def Soummision(request):
    return render(request,'pages/soumission.html')



def inscription_entrepreneur(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        entreprise_form = EntrepriseForm(request.POST, request.FILES)
        if user_form.is_valid() and entreprise_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            entreprise = entreprise_form.save(commit=False)
            entreprise.user = user
            entreprise.save()
            return redirect(home)
    else:
        user_form = UserForm()
        entreprise_form = EntrepriseForm()
    return render(request, 'pages/inscription_entrepreneur.html', {
        'user_form': user_form,
        'entreprise_form': entreprise_form
    })
    
    

def inscription_client(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            return redirect('home')  # Ensure you have a view named 'home'
    else:
        user_form = UserForm()
        client_form = ClientForm()
    return render(request, 'pages/inscription_client.html', {
        'user_form': user_form,
        'client_form': client_form
    })
    
def contact(request):
    return render(request,'main/contact.html')

def Affiliation(request):
    return render(request,'pages/affiliation.html')



def cgu(request):
    return render(request,'pages/cgu.html')