from django.urls import path
from base.views import Affiliation, Soummision, activate_forfait, blog, blog_details, cgu,contact, details_soumission, entreprises_par_service, forfaits, home, inscription_client, inscription_entrepreneur, login_view, logout_view, profile, profile_entreprise, repertoire, search_view, services, soumission_success

urlpatterns = [
    path('',home,name="home"),
    path('services',services),
    path('forfaits',forfaits),
    path('repertoire',repertoire),
    path('post/<slug:slug>',blog_details,name="detail_blog"),
    path('blogue',blog,name="blog"),
    path('contact',contact),
    path('search/', search_view, name='search'),
    path('activate_forfait',activate_forfait),
    path('Soummision',Soummision),
    path('entreprise/<slug:slug>/',profile_entreprise,name="entreprise_detail"),
    path('Affiliation',Affiliation),
    path('connexion',login_view,name="login"),
    path('details_soumission/<int:id>/',details_soumission,name="details_soumission"),
    path('inscription-entrepreneur',inscription_entrepreneur,name="inscription_entrepreneur"),
    path('client',inscription_client,name="inscription_client"),
    path('cgu',cgu),
    path('logout/', logout_view, name='logout'),  # URL pour la déconnexion
    path('profile',profile),
    path('soumission_success',soumission_success),
    path('service/<slug:slug>/entreprises',entreprises_par_service,name="detail_service"),
]