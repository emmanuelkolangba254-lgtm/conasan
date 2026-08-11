from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
path(
    "connexion/",
    views.connexion,
    name="connexion"
),

path(
    "deconnexion/",
    views.deconnexion,
    name="deconnexion"
),

    path('', views.index, name='home'),

    path('apropos/', views.apropos, name='apropos'),

    path('programmes/', views.programmes, name='programmes'),

    path('structures/', views.structures, name='structures'),

    path('gouvernance/', views.gouvernance, name='gouvernance'),

    path('actualites/', views.actualites, name='actualites'),

    path('partenaires/', views.partenaires, name='partenaires'),

    path('documentation/', views.documentation, name='documentation'),

    path('contact/', views.contact, name='contact'),

    path(
        'contact/<int:id>/',
        views.detail_message,
        name='detail_message'
    ),

    path(
        'contact/<int:id>/supprimer/',
        views.supprimer_message,
        name='supprimer_message'
    ),

    path(
        'api/structures/',
        views.api_structures,
        name='api_structures'
    ),

    path(
        'structure/<int:id>/',
        views.detail_structure,
        name='detail_structure'
    ),

    path(
        'actualite/<int:id>/',
        views.detail_actualite,
        name='detail_actualite'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

path(
    'utilisateurs/',
    views.utilisateurs,
    name='utilisateurs'
),
path(
    "api/recherche/",
    views.recherche_intelligente,
    name="recherche_intelligente"
),
path(
    "dashboard/programmes/",
    views.dashboard_programmes,
    name="dashboard_programmes"
),
path(
    "dashboard/programmes/",
    views.dashboard_programmes,
    name="dashboard_programmes"
),
path(
    "dashboard/programmes/",
    views.dashboard_programmes,
    name="dashboard_programmes"
),

path(
    "dashboard/programmes/ajouter/",
    views.ajouter_programme,
    name="ajouter_programme"
),

path(
    "dashboard/programmes/modifier/<int:id>/",
    views.modifier_programme,
    name="modifier_programme"
),

path(
    "dashboard/programmes/supprimer/<int:id>/",
    views.supprimer_programme,
    name="supprimer_programme"
),
path(
    "dashboard/actualites/",
    views.dashboard_actualites,
    name="dashboard_actualites"
),
path('actualites/ajouter/', views.ajouter_actualite, name='ajouter_actualite'),
path(
    'dashboard/actualites/modifier/<int:id>/',
    views.modifier_actualite,
    name='modifier_actualite'
),
path(
    'dashboard/actualites/supprimer/<int:id>/',
    views.supprimer_actualite,
    name='supprimer_actualite'
),
path(
    "dashboard/structures/",
    views.dashboard_structures,
    name="dashboard_structures"
),

path(
    "dashboard/structures/ajouter/",
    views.ajouter_structure,
    name="ajouter_structure"
),

path(
    "dashboard/structures/modifier/<int:id>/",
    views.modifier_structure,
    name="modifier_structure"
),

path(
    "dashboard/structures/supprimer/<int:id>/",
    views.supprimer_structure,
    name="supprimer_structure"
),
path(
    "dashboard/apropos/",
    views.dashboard_apropos,
    name="dashboard_apropos"
),

path(
    "dashboard/apropos/ajouter/",
    views.ajouter_apropos,
    name="ajouter_apropos"
),

path(
    "dashboard/apropos/modifier/<int:id>/",
    views.modifier_apropos,
    name="modifier_apropos"
),

path(
    "dashboard/apropos/supprimer/<int:id>/",
    views.supprimer_apropos,
    name="supprimer_apropos"
),
path(
    "apropos/<str:section>/",
    views.detail_apropos,
    name="detail_apropos"
),
path(
    "dashboard/gouvernance/",
    views.dashboard_gouvernance,
    name="dashboard_gouvernance",
),

path(
    "dashboard/gouvernance/ajouter/",
    views.ajouter_dirigeant,
    name="ajouter_dirigeant",
),
# GOUVERNANCE

path(
    "dashboard/gouvernance/",
    views.dashboard_gouvernance,
    name="dashboard_gouvernance",
),

path(
    "dashboard/gouvernance/ajouter/",
    views.ajouter_dirigeant,
    name="ajouter_dirigeant",
),

path(
    "dashboard/gouvernance/modifier/<int:id>/",
    views.modifier_dirigeant,
    name="modifier_dirigeant",
),

path(
    "dashboard/gouvernance/supprimer/<int:id>/",
    views.supprimer_dirigeant,
    name="supprimer_dirigeant",
),
# PARTENAIRES

path(
    "dashboard/partenaires/",
    views.dashboard_partenaires,
    name="dashboard_partenaires",
),

path(
    "dashboard/partenaires/ajouter/",
    views.ajouter_partenaire,
    name="ajouter_partenaire",
),

path(
    "dashboard/partenaires/modifier/<int:id>/",
    views.modifier_partenaire,
    name="modifier_partenaire",
),

path(
    "dashboard/partenaires/supprimer/<int:id>/",
    views.supprimer_partenaire,
    name="supprimer_partenaire",
),
path(
    "dashboard/documentation/",
    views.dashboard_documentation,
    name="dashboard_documentation",
),

path(
    "dashboard/galerie/",
    views.dashboard_galerie,
    name="dashboard_galerie"
),
# GALERIE

path(
    "dashboard/galerie/",
    views.dashboard_galerie,
    name="dashboard_galerie",
),

# VIDEOS

path(
    "dashboard/videos/",
    views.dashboard_videos,
    name="dashboard_videos",
),

# NOTIFICATIONS

path(
    "dashboard/notifications/",
    views.dashboard_notifications,
    name="dashboard_notifications",
),

# TRADUCTIONS

path(
    "dashboard/traductions/",
    views.dashboard_traductions,
    name="dashboard_traductions",
),

# IA

path(
    "dashboard/intelligence-artificielle/",
    views.dashboard_ia,
    name="dashboard_ia",
),

# PARAMETRES

path(
    "dashboard/parametres/",
    views.dashboard_parametres,
    name="dashboard_parametres",
),

# JOURNAL

path(
    "dashboard/journal/",
    views.dashboard_journal,
    name="dashboard_journal",
),

# GPS

path(
    "dashboard/gps/",
    views.dashboard_gps,
    name="dashboard_gps",
),
path(
    "dashboard/galerie/",
    views.dashboard_galerie,
    name="dashboard_galerie"
),

path(
    "dashboard/galerie/ajouter/",
    views.ajouter_photo,
    name="ajouter_photo"
),

path(
    "dashboard/galerie/modifier/<int:id>/",
    views.modifier_photo,
    name="modifier_photo"
),

path(
    "dashboard/galerie/supprimer/<int:id>/",
    views.supprimer_photo,
    name="supprimer_photo"
),
path(
    "dashboard/messages/",
    views.messages_dashboard,
    name="messages_dashboard",
),
path(
    "logout/",
    LogoutView.as_view(next_page="/"),
    name="logout",
),
path(
    "dashboard/hero/",
    views.dashboard_hero,
    name="dashboard_hero",
),

path(
    "dashboard/hero/modifier/",
    views.modifier_hero,
    name="modifier_hero",
),
path(
    "dashboard/documentation/",
    views.dashboard_documentation,
    name="dashboard_documentation"
),

path(
    "dashboard/documentation/ajouter/",
    views.ajouter_documentation,
    name="ajouter_documentation"
),

path(
    "dashboard/documentation/modifier/<int:pk>/",
    views.modifier_documentation,
    name="modifier_documentation"
),

path(
    "dashboard/documentation/supprimer/<int:pk>/",
    views.supprimer_documentation,
    name="supprimer_documentation"
),
path(
    "connexion/",
    auth_views.LoginView.as_view(
        template_name="login.html",
        redirect_authenticated_user=True
    ),
    name="connexion"
),

path(
    "deconnexion/",
    auth_views.LogoutView.as_view(
        next_page="/connexion/"
    ),
    name="deconnexion"
),
]
