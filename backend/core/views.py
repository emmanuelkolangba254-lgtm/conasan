from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from contenu.models import Contact
from contenu.models import Notification
from django.shortcuts import redirect
from contenu.models import Apropos
from contenu.models import Document
from contenu.models import Hero
from contenu.forms import HeroForm
from contenu.models import HeroAccueil
from contenu.forms import GalerieForm, GouvernanceDocumentForm
from contenu.models import (
    Dirigeant,
    DocumentOrganigramme,
    GouvernanceDocument,
)
from contenu.forms import DirigeantForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def admin_conasan_required(view_func):
    return user_passes_test(
        lambda user: user.is_authenticated and (
            user.is_superuser or
            user.groups.filter(name="ADMIN_CONASAN").exists()
        )
    )(view_func)
from contenu.models import Programme, Actualite, Partenaire, StructureSanitaire
from contenu.models import Profil
from django.contrib.auth import logout
from django.shortcuts import redirect
from contenu.models import Galerie
from django.shortcuts import render, redirect, get_object_or_404
def deconnexion(request):
    logout(request)
    return redirect("/")
from django.contrib.auth.decorators import user_passes_test
from contenu.permissions import (
    est_superadmin,
    est_admin,
    est_agent
)
from contenu.forms import (
    DirigeantForm,
    CODISForm,
    DocumentOrganigrammeForm,
)
from contenu.models import Dirigeant
from contenu.models import (
    Dirigeant,
    CODIS,
    DocumentOrganigramme,
)
from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
def connexion(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        messages.error(
            request,
            "Nom d'utilisateur ou mot de passe incorrect."
        )

    return render(
        request,
        "login.html"
    )
def deconnexion(request):

    logout(request)

    return redirect("home")
def dashboard_required(view_func):

    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):

        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        if request.user.groups.filter(
            name="ADMIN_CONASAN"
        ).exists():
            return view_func(request, *args, **kwargs)

        return redirect("connexion")

    return wrapper
def index(request):

    programmes = Programme.objects.all()[:6]

    actualites = Actualite.objects.all().order_by('-date_publication')[:6]

    partenaires = Partenaire.objects.all()
    galerie = Galerie.objects.filter(
    publier=True
).order_by("-date_creation")[:4]

    structures = StructureSanitaire.objects.all()
    hero = HeroAccueil.objects.filter(actif=True).first()

    context = {
        'programmes': programmes,
        'actualites': actualites,
        'partenaires': partenaires,
        'structures': structures,
        "nb_users": User.objects.count(),
        "hero": hero,
        "galerie": galerie,
    }

    return render(request, "index.html", context)

from contenu.models import Apropos

def apropos(request):

    contenu = Apropos.objects.first()

    return render(
        request,
        "apropos.html",
        {
            "contenu": contenu
        }
    )
def programmes(request):
    return render(request, "programmes.html")

def structures(request):

    structures = StructureSanitaire.objects.all()

    return render(
        request,
        'structures.html',
        {
            'structures': structures
        }
    )
def gouvernance(request):

    dirigeants = Dirigeant.objects.filter(
        actif=True
    ).order_by("ordre")

    organigrammes = DocumentOrganigramme.objects.all().order_by(
        "-date_creation"
    )

    documents = GouvernanceDocument.objects.filter(
        publier=True
    ).order_by("-date_creation")

    return render(
        request,
        "gouvernance.html",
        {
            "dirigeants": dirigeants,
            "organigrammes": organigrammes,
            "documents": documents,
        }
    )

def actualites(request):

    actualites = Actualite.objects.all().order_by(
        '-date_publication'
    )

    return render(
        request,
        "actualites.html",
        {
            "actualites": actualites
        }
    )
def partenaires(request):
    partenaires = Partenaire.objects.all().order_by("nom")

    return render(
    request,
    "partenaires.html",
    {
        "partenaires": partenaires,
    }
    )

def documentation(request):
    return render(request, "documentation.html")

def contact(request):

    if request.method == "POST":

        Contact.objects.create(
            nom=request.POST.get('nom'),
            email=request.POST.get('email'),
            sujet=request.POST.get('sujet'),
            message=request.POST.get('message')
        )

        admins = User.objects.filter(
            is_staff=True
        )

        for admin in admins:

            Notification.objects.create(
                utilisateur=admin,
                titre="Nouveau message",
                message=f"""
Nouveau message reçu :
{request.POST.get('sujet')}
"""
            )

        messages.success(
            request,
            "Votre message a été envoyé avec succès."
        )

    return render(
        request,
        "contact.html"
    )
def api_structures(request):

    structures = StructureSanitaire.objects.all()

    data = []

    for s in structures:

        data.append({
            'id': s.id,
            'nom': s.nom,
            'telephone': s.telephone,
            'latitude': s.latitude,
            'longitude': s.longitude,
            'ville': getattr(s, 'ville', ''),
        })

    return JsonResponse(data, safe=False)
def detail_structure(request, id):

    structure = get_object_or_404(
        StructureSanitaire,
        id=id
    )

    return render(
        request,
        "detail_structure.html",
        {
            "structure": structure
        }
    )
def detail_actualite(request, id):

    actualite = get_object_or_404(
        Actualite,
        id=id
    )

    return render(
        request,
        'detail_actualite.html',
        {
            'actualite': actualite
        }
    )

@login_required
def dashboard(request):

    notifications = Notification.objects.filter(
        utilisateur=request.user
    ).order_by('-date_creation')

    messages_contact = Contact.objects.order_by("-id")[:10]

    nb_notifications = Notification.objects.filter(
        utilisateur=request.user,
        lu=False
    ).count()

    context = {

        'nb_programmes': Programme.objects.count(),

        'nb_actualites': Actualite.objects.count(),

        'nb_structures': StructureSanitaire.objects.count(),

        'nb_partenaires': Partenaire.objects.count(),

        'nb_users': User.objects.count(),

        'notifications': notifications[:10],

        'nb_notifications': nb_notifications,
        'messages_contact': messages_contact,

    }

    return render(
        request,
        'dashboard.html',
        context
    )
@login_required
def detail_message(request, id):

    message = get_object_or_404(
        Contact,
        id=id
    )

    if request.method == "POST":

        action = request.POST.get("action")

        if action == "lu":
            message.statut = "Lu"

        elif action == "archive":
            message.archive = True

        elif action == "corbeille":
            message.corbeille = True

        elif action == "repondre":

            message.reponse = request.POST.get(
                "reponse"
            )

            message.statut = "Répondu"

        elif action == "transfert":

            message.transfert = request.POST.get(
                "transfert"
            )

            message.statut = "Transféré"

        message.save()

        return redirect(
            "detail_message",
            id=message.id
        )

    return render(
        request,
        "detail_message.html",
        {
            "message": message
        }
    )
from django.shortcuts import redirect

@login_required
def supprimer_message(request, id):

    message = get_object_or_404(
        Contact,
        id=id
    )

    message.delete()

    return redirect(
        'dashboard'
    )
@login_required
def utilisateurs(request):

    utilisateurs = User.objects.all().select_related("profil")

    return render(
        request,
        "utilisateurs.html",
        {
            "utilisateurs": utilisateurs
        }
    )
from django.http import JsonResponse
from contenu.models import StructureSanitaire
from contenu.models import Programme
from contenu.models import Actualite

def recherche_intelligente(request):

    q = request.GET.get("q", "").strip()

    resultats = []

    if q:

        structures = StructureSanitaire.objects.filter(
            nom__icontains=q
        )[:5]

        for s in structures:

            resultats.append({

                "type": "Structure",

                "nom": s.nom,

                "url": f"/structure/{s.id}/"

            })

        programmes = Programme.objects.filter(
            titre__icontains=q
        )[:5]

        for p in programmes:

            resultats.append({

                "type": "Programme",

                "nom": p.titre,

                "url": "/programmes/"

            })

        actualites = Actualite.objects.filter(
            titre__icontains=q
        )[:5]

        for a in actualites:

            resultats.append({

                "type": "Actualité",

                "nom": a.titre,

                "url": f"/actualite/{a.id}/"

            })

    return JsonResponse(resultats, safe=False)
@login_required
def dashboard_programmes(request):

    programmes = Programme.objects.all().order_by("-id")

    return render(
        request,
        "dashboard_programmes.html",
        {
            "programmes": programmes
        }
    )
@login_required
def dashboard_programmes(request):

    programmes = Programme.objects.all().order_by("-id")

    return render(
        request,
        "dashboard_programmes.html",
        {
            "programmes": programmes
        }
    )
from django.forms import modelform_factory

ProgrammeForm = modelform_factory(
    Programme,
    exclude=[]
)

@login_required
def dashboard_programmes(request):

    programmes = Programme.objects.all().order_by("-id")

    return render(
        request,
        "dashboard_programmes.html",
        {
            "programmes": programmes
        }
    )


@login_required
def ajouter_programme(request):

    form = ProgrammeForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        form.save()

        return redirect("dashboard_programmes")

    return render(
        request,
        "programme_form.html",
        {
            "form": form,
            "titre": "Ajouter un programme"
        }
    )


@login_required
def modifier_programme(request,id):

    programme=get_object_or_404(
        Programme,
        id=id
    )

    form=ProgrammeForm(
        request.POST or None,
        request.FILES or None,
        instance=programme
    )

    if form.is_valid():

        form.save()

        return redirect("dashboard_programmes")

    return render(
        request,
        "programme_form.html",
        {
            "form":form,
            "titre":"Modifier le programme"
        }
    )


@login_required
def supprimer_programme(request,id):

    programme=get_object_or_404(
        Programme,
        id=id
    )

    programme.delete()

    return redirect("dashboard_programmes")
@login_required
def dashboard_actualites(request):

    actualites = Actualite.objects.all().order_by("-date_publication")

    return render(
        request,
        "dashboard_actualites.html",
        {
            "actualites": actualites
        }
    )

@login_required
def ajouter_actualite(request):
    return render(request, "dashboard/ajouter_actualite.html")
@login_required
def modifier_actualite(request, id):
    return render(
        request,
        "dashboard/modifier_actualite.html",
        {"id": id}
    )
@login_required
def supprimer_actualite(request, id):
    return render(
        request,
        "dashboard/supprimer_actualite.html",
        {"id": id}
    )
# ===========================
# GESTION DES STRUCTURES
# ===========================

@login_required
def dashboard_structures(request):

    structures = StructureSanitaire.objects.all().order_by("-id")

    return render(
        request,
        "dashboard_structures.html",
        {
            "structures": structures
        }
    )


@login_required
def ajouter_structure(request):

    return render(
        request,
        "ajouter_structure.html"
    )


@login_required
def modifier_structure(request, id):

    return render(
        request,
        "modifier_structure.html"
    )


@login_required
def supprimer_structure(request, id):

    return redirect(
        "dashboard_structures"
    )
@login_required
def dashboard_apropos(request):

    apropos = Apropos.objects.all()

    return render(
        request,
        "dashboard_apropos.html",
        {
            "apropos": apropos
        }
    )
@login_required
def ajouter_apropos(request):

    if request.method == "POST":

        Apropos.objects.create(

            titre=request.POST["titre"],

            description=request.POST["description"],

            mission=request.POST["mission"],

            vision=request.POST["vision"],

            image=request.FILES.get("image")

        )

        return redirect("dashboard_apropos")

    return render(
        request,
        "ajouter_apropos.html"
    )
@login_required
def modifier_apropos(request,id):

    apropos=get_object_or_404(Apropos,id=id)

    if request.method=="POST":

        apropos.titre=request.POST["titre"]

        apropos.description=request.POST["description"]

        apropos.mission=request.POST["mission"]

        apropos.vision=request.POST["vision"]

        if request.FILES.get("image"):
            apropos.image=request.FILES["image"]

        apropos.save()

        return redirect("dashboard_apropos")

    return render(
        request,
        "modifier_apropos.html",
        {
            "apropos":apropos
        }
    )
@login_required
def supprimer_apropos(request,id):

    apropos=get_object_or_404(Apropos,id=id)

    apropos.delete()

    return redirect("dashboard_apropos")

def detail_apropos(request, section):

    apropos = Apropos.objects.first()

    if section == "mission":
        contexte = {
            "titre": "Notre Mission",
            "contenu": apropos.mission,
            "image": apropos.image_mission,
            "document": apropos.document_mission,
        }

    elif section == "vision":
        contexte = {
            "titre": "Notre Vision",
            "contenu": apropos.vision,
            "image": apropos.image_vision,
            "document": apropos.document_vision,
        }

    elif section == "valeurs":
        contexte = {
            "titre": "Nos Valeurs",
            "contenu": apropos.valeurs,
            "image": apropos.image_valeurs,
            "document": apropos.document_valeurs,
        }

    else:
        contexte = {
            "titre": "Notre Engagement",
            "contenu": apropos.engagement,
            "image": apropos.image_engagement,
            "document": apropos.document_engagement,
        }

    return render(
        request,
        "detail_apropos.html",
        contexte
    )
@login_required
def detail_apropos_admin(request):
    contenu = Apropos.objects.first()

    return render(
        request,
        "dashboard_apropos.html",
        {
            "contenu": contenu
        }
    )
def detail_apropos(request, section):

    contenu = Apropos.objects.first()

    if contenu is None:
        return render(
            request,
            "detail_apropos.html",
            {
                "titre": "Information indisponible",
                "contenu": ""
            }
        )

    donnees = {
        "mission": ("Notre Mission", contenu.mission),
        "vision": ("Notre Vision", contenu.vision),
        "valeurs": ("Nos Valeurs", contenu.valeurs),
        "engagement": ("Notre Engagement", contenu.engagement),
    }

    titre, texte = donnees.get(
        section,
        ("À propos", contenu.description)
    )

    return render(
        request,
        "detail_apropos.html",
        {
            "titre": titre,
            "contenu": texte,
        }
    )
@login_required
def dashboard_gouvernance(request):

    dirigeants = Dirigeant.objects.all().order_by("ordre")

    organigramme = GouvernanceDocument.objects.filter(
        type_document="organigramme"
    ).first()

    return render(
        request,
        "dashboard_gouvernance.html",
        {
            "dirigeants": dirigeants,
            "organigramme": organigramme,
        }
    )          
# ==========================================
# GOUVERNANCE
# ==========================================

@login_required
def ajouter_dirigeant(request):
    if request.method == "POST":
        form = DirigeantForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard_gouvernance")
    else:
        form = DirigeantForm()

    return render(
        request,
        "ajouter_dirigeant.html",
        {
            "form": form
        }
    )
@login_required
def modifier_dirigeant(request,id):

    dirigeant = get_object_or_404(
        Dirigeant,
        id=id
    )

    if request.method == "POST":

        form = DirigeantForm(
            request.POST,
            request.FILES,
            instance=dirigeant
        )

        if form.is_valid():

            form.save()

            return redirect("dashboard_gouvernance")

    else:

        form = DirigeantForm(
            instance=dirigeant
        )

    return render(
        request,
        "modifier_dirigeant.html",
        {
            "form":form
        }
    )


@login_required
def supprimer_dirigeant(request,id):

    dirigeant=get_object_or_404(
        Dirigeant,
        id=id
    )

    dirigeant.delete()

    return redirect("dashboard_gouvernance")

def gouvernance(request):

    dirigeants = Dirigeant.objects.filter(
        actif=True
    ).order_by("ordre")

    organigramme = GouvernanceDocument.objects.filter(
        type_document="organigramme"
    ).first()

    documents = GouvernanceDocument.objects.exclude(
        type_document="organigramme"
    )

    return render(
        request,
        "gouvernance.html",
        {
            "dirigeants": dirigeants,
            "documents": documents,
            "organigramme_image": organigramme.image_apercu if organigramme else None,
            "organigramme_pdf": organigramme.fichier if organigramme else None,
        },
    )

@login_required
def modifier_dirigeant(request, id):

    dirigeant = get_object_or_404(
        Dirigeant,
        id=id,
    )

    if request.method == "POST":

        dirigeant.nom = request.POST.get("nom")

        dirigeant.fonction = request.POST.get("fonction")

        dirigeant.telephone = request.POST.get("telephone")

        dirigeant.email = request.POST.get("email")

        dirigeant.ordre = request.POST.get("ordre")

        if request.FILES.get("photo"):

            dirigeant.photo = request.FILES.get("photo")

        dirigeant.save()

        return redirect(
            "dashboard_gouvernance"
        )

    return render(
        request,
        "modifier_dirigeant.html",
        {
            "dirigeant": dirigeant
        }
    )
@login_required
def supprimer_dirigeant(request, id):

    dirigeant = get_object_or_404(
        Dirigeant,
        id=id,
    )

    dirigeant.delete()

    return redirect(
        "dashboard_gouvernance"
    )
@login_required
def dashboard_partenaires(request):

    partenaires = Partenaire.objects.all().order_by("nom")

    return render(
        request,
        "dashboard_partenaires.html",
        {
            "partenaires": partenaires
        }
    )


@login_required
def ajouter_partenaire(request):

    if request.method == "POST":

        Partenaire.objects.create(

            nom=request.POST.get("nom"),

            description=request.POST.get("description"),

            site_web=request.POST.get("site_web"),

            logo=request.FILES.get("logo"),
        )

        return redirect("dashboard_partenaires")

    return render(
        request,
        "ajouter_partenaire.html",
    )


@login_required
def modifier_partenaire(request,id):

    partenaire=get_object_or_404(
        Partenaire,
        id=id
    )

    if request.method=="POST":

        partenaire.nom=request.POST.get("nom")

        partenaire.description=request.POST.get("description")

        partenaire.site_web=request.POST.get("site_web")

        if request.FILES.get("logo"):

            partenaire.logo=request.FILES.get("logo")

        partenaire.save()

        return redirect(
            "dashboard_partenaires"
        )

    return render(
        request,
        "modifier_partenaire.html",
        {
            "partenaire":partenaire
        }
    )


@login_required
def supprimer_partenaire(request,id):

    partenaire=get_object_or_404(
        Partenaire,
        id=id
    )

    partenaire.delete()

    return redirect(
        "dashboard_partenaires"
    )
@login_required
def dashboard_documentation(request):

    documents = Document.objects.all().order_by("-id")

    return render(
        request,
        "dashboard_documentation.html",
        {
            "documents": documents
        }
    )
@login_required
def ajouter_document(request):

    if request.method == "POST":

        Document.objects.create(

            titre=request.POST.get("titre"),

            categorie=request.POST.get("categorie"),

            description=request.POST.get("description"),

            image=request.FILES.get("image"),

            fichier=request.FILES.get("fichier"),

            public=True if request.POST.get("public") else False

        )

        return redirect("dashboard_documentation")

    return render(
        request,
        "ajouter_document.html"
    )
@login_required
def modifier_document(request, id):

    document = get_object_or_404(
        Document,
        id=id
    )

    if request.method == "POST":

        document.titre = request.POST.get("titre")

        document.categorie = request.POST.get("categorie")

        document.description = request.POST.get("description")

        document.public = True if request.POST.get("public") else False

        if request.FILES.get("image"):
            document.image = request.FILES.get("image")

        if request.FILES.get("fichier"):
            document.fichier = request.FILES.get("fichier")

        document.save()

        return redirect(
            "dashboard_documentation"
        )

    return render(
        request,
        "modifier_document.html",
        {
            "document": document
        }
    )
@login_required
def supprimer_document(request, id):

    document = get_object_or_404(
        Document,
        id=id
    )

    document.delete()

    return redirect(
        "dashboard_documentation"
    )

@login_required
def dashboard_videos(request):

    return render(
        request,
        "dashboard_videos.html"
    )


@login_required
def dashboard_notifications(request):

    return render(
        request,
        "dashboard_notifications.html"
    )


@login_required
def dashboard_traductions(request):

    return render(
        request,
        "dashboard_traductions.html"
    )


@login_required
def dashboard_ia(request):

    return render(
        request,
        "dashboard_ia.html"
    )


@login_required
def dashboard_parametres(request):

    return render(
        request,
        "dashboard_parametres.html"
    )


@login_required
def dashboard_journal(request):

    return render(
        request,
        "dashboard_journal.html"
    )


@login_required
def dashboard_gps(request):

    return render(
        request,
        "dashboard_gps.html"
    )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from contenu.models import Galerie
from contenu.forms import GalerieForm
@login_required
def dashboard_galerie(request):
    photos = Galerie.objects.all().order_by("-date_creation")

    return render(
        request,
        "dashboard_galerie.html",
        {
            "galerie": photos,
        }
    )

@login_required
def ajouter_photo(request):
    if request.method == "POST":
        form = GalerieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard_galerie")
    else:
        form = GalerieForm()

    return render(
        request,
        "ajouter_photo.html",
        {"form": form},
    )


@login_required
def modifier_photo(request, pk):
    photo = get_object_or_404(Galerie, pk=pk)

    if request.method == "POST":
        form = GalerieForm(
            request.POST,
            request.FILES,
            instance=photo,
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard_galerie")

    else:
        form = GalerieForm(instance=photo)

    return render(
        request,
        "modifier_photo.html",
        {
            "form": form,
            "photo": photo,
        },
    )


@login_required
def supprimer_photo(request, pk):
    photo = get_object_or_404(Galerie, pk=pk)

    if request.method == "POST":
        photo.delete()
        return redirect("dashboard_galerie")

    return render(
        request,
        "supprimer_photo.html",
        {
            "photo": photo,
        },
    )
from django.contrib.auth.decorators import login_required

@login_required
def messages_dashboard(request):
    return render(request, "dashboard_messages.html")
@login_required
def dashboard_hero(request):
    hero = Hero.objects.first()

    return render(
        request,
        "dashboard_hero.html",
        {"hero": hero},
    )
@login_required
def modifier_hero(request):

    hero = Hero.objects.first()

    if not hero:
        hero = Hero.objects.create(
            titre="Agir ensemble pour la santé intégrale",
            sous_titre="La CONASAN œuvre pour la santé..."
        )

    if request.method == "POST":
        form = HeroForm(request.POST, request.FILES, instance=hero)

        if form.is_valid():
            form.save()
            return redirect("dashboard_hero")

    else:
        form = HeroForm(instance=hero)

    return render(
        request,
        "modifier_hero.html",
        {"form": form},
    )
@login_required
def supprimer_photo(request, pk):

    photo = get_object_or_404(
        Galerie,
        pk=pk
    )

    if request.method == "POST":

        photo.delete()

        return redirect("dashboard_galerie")

    return render(
        request,
        "supprimer_photo.html",
        {
            "photo": photo
        }
    )
# ==========================================================
# DOCUMENTATION - GESTION DES DOCUMENTS
# ==========================================================

@login_required
def dashboard_documentation(request):

    documents = GouvernanceDocument.objects.all().order_by("-date_creation")

    return render(
        request,
        "dashboard_documentation.html",
        {
            "documents": documents,
        }
    )


@login_required
def ajouter_documentation(request):

    if request.method == "POST":

        form = GouvernanceDocumentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect("dashboard_documentation")

    else:

        form = GouvernanceDocumentForm()

    return render(
        request,
        "ajouter_documentation.html",
        {
            "form": form,
        }
    )


@login_required
def modifier_documentation(request, pk):

    document = get_object_or_404(
        GouvernanceDocument,
        pk=pk
    )

    if request.method == "POST":

        form = GouvernanceDocumentForm(
            request.POST,
            request.FILES,
            instance=document
        )

        if form.is_valid():

            form.save()

            return redirect("dashboard_documentation")

    else:

        form = GouvernanceDocumentForm(
            instance=document
        )

    return render(
        request,
        "modifier_documentation.html",
        {
            "form": form,
            "document": document,
        }
    )


@login_required
def supprimer_documentation(request, pk):

    document = get_object_or_404(
        GouvernanceDocument,
        pk=pk
    )

    if request.method == "POST":

        document.delete()

        return redirect("dashboard_documentation")

    return render(
        request,
        "supprimer_documentation.html",
        {
            "document": document,
        }
    )
