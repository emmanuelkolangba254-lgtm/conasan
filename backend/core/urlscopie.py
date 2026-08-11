from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),   # 👈 IMPORTANT
    path('apropos/', views.apropos, name='apropos'),
    path('programmes/', views.programmes, name='programmes'),
    path('actualites/', views.actualites, name='actualites'),
    path('partenaires/', views.partenaires, name='partenaires'),
    path('contact/', views.contact, name='contact'),
]
