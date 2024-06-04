from django.urls import path
from base.views import Soummision, blog, blog_details, contact, details_soumission, forfaits, home, inscription_client, inscription_entrepreneur, repertoire, services

urlpatterns = [
    path('',home,name="home"),
    path('services',services),
    path('forfaits',forfaits),
    path('repertoire',repertoire),
    path('post/<slug:slug>',blog_details,name="detail_blog"),
    path('blogue',blog,name="blog"),
    path('contact',contact),
    path('Soummision',Soummision),
    path('details_soumission/<int:id>/',details_soumission,name="details_soumission"),
    path('inscription-entrepreneur',inscription_entrepreneur,name="inscription_entrepreneur"),
    path('client',inscription_client,name="inscription_client")
]