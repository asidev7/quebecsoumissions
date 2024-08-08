from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login
from base.forms import SoumissionForm
from base.models import Blog, Entreprise, Forfait, Realisation, Service, Type_Soumission
from .forms import ClientForm, ContactForm, SearchForm, UserForm, EntrepriseForm
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import logout


# Create your views here.
def home(request):
    categories = Service.objects.all()[:9]
    services = Service.objects.all()[:9]

    blogs = Blog.objects.all()
    chunked_blogs = [blogs[i:i + 3] for i in range(0, len(blogs), 3)]
    realisations = Realisation.objects.all()

    params ={
        'services':services,
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
    forfaits = Forfait.objects.all().prefetch_related('fonctionnalites')
    nbr_forfaits = Forfait.objects.all().count
    params ={
        'forfaits':forfaits,
        'nbr_forfaits':nbr_forfaits
    }
    return render(request,'pages/forfaits.html',params)

@login_required
def activate_forfait(request):
    return render(request,'pages/activate.html')


def repertoire(request):
    entreprises = Entreprise.objects.all()
    services = Service.objects.all()

    params ={
        'entreprises':entreprises,
        'services':services
    }
    return render(request,'pages/repertoire.html',params)

def entreprises_par_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    entreprises = Entreprise.objects.filter(service=service)
    context = {
        'service': service,
        'entreprises': entreprises
    }
    return render(request,'pages/entreprise_list_service.html',context)

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
    if request.method == 'POST':
        form = SoumissionForm(request.POST)
        if form.is_valid():
            soumission = form.save(commit=False)
            if request.user.is_authenticated:
                soumission.user = request.user
            soumission.save()
            return redirect(soumission_success)  # Redirige vers une page de succès ou une autre page
    else:
        form = SoumissionForm()
    params ={
        'form':form
    }
    return render(request,'pages/soumission.html',params)

def soumission_success(request):
    return render(request,'pages/soumission_success.html')

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


def profile_entreprise(request,slug):
    entreprise = get_object_or_404(Entreprise, slug=slug)
    params ={
        'entreprise':entreprise
    }
    return render(request,'pages/profile-entreprise.html',params)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(home)  # Redirige vers la page d'accueil ou une autre page après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect(home)
    else:
        form = ContactForm()
    params ={
        'form':form
    }
    return render(request,'main/contact.html',params)

def Affiliation(request):
    return render(request,'pages/affiliation.html')



def cgu(request):
    return render(request,'pages/cgu.html')


def search_view(request):
    query = request.GET.get('query')
    entreprises = []
    services = []
    if query:
        entreprises = Entreprise.objects.filter(
            Q(description_courte__icontains=query) |
            Q(texte_presentation__icontains=query) |
            Q(avantages__icontains=query) |
            Q(courte_description_entreprise__icontains=query) |
            Q(user__username__icontains=query)
        )
        services = Service.objects.filter(nom__icontains=query)
    
    return render(request, 'main/search_results.html', {'query': query, 'entreprises': entreprises, 'services': services})


@login_required
def profile(request):
    user = request.user
    entreprise = Entreprise.objects.get(user=user)
    if request.method == 'POST':
        form = EntrepriseForm(request.POST, request.FILES, instance=entreprise)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EntrepriseForm(instance=entreprise)
    params ={
        'form':form,
        'user': user, 
        'entreprise': entreprise
    }
    return render(request, 'pages/profile.html', params)


def logout_view(request):
    logout(request)
    return redirect(home)  # Redirige vers la page d'accueil ou une autre page après déconnexion