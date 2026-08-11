from django.db import models
from geopy.geocoders import Nominatim
from django.contrib.auth.models import User
class Programme(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()

    image1 = models.ImageField(
        upload_to='programmes/'
    )

    image2 = models.ImageField(
        upload_to='programmes/',
        blank=True,
        null=True
    )

    image3 = models.ImageField(
        upload_to='programmes/',
        blank=True,
        null=True
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre

class Actualite(models.Model):

    titre=models.CharField(max_length=250)

    resume=models.TextField()

    contenu=models.TextField()

    image=models.ImageField(upload_to="actualites/")

    categorie=models.CharField(
        max_length=120,
        default="Santé"
    )

    auteur=models.CharField(
        max_length=100,
        default="CONASAN"
    )

    vues=models.PositiveIntegerField(
        default=0
    )

    vedette=models.BooleanField(
        default=False
    )

    date_publication=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre
class Partenaire(models.Model):
    nom = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='partenaires/')
    site_web = models.URLField(blank=True)

    def __str__(self):
        return self.nom


PREFECTURES = [
    ("Bangui", "Bangui"),
    ("Ombella-Mpoko", "Ombella-Mpoko"),
    ("Lobaye", "Lobaye"),
    ("Mambere-Kadei", "Mambere-Kadei"),
    ("Nana-Mambere", "Nana-Mambere"),
    ("Sangha-Mbaere", "Sangha-Mbaere"),
    ("Kemo", "Kemo"),
    ("Ouaka", "Ouaka"),
    ("Basse-Kotto", "Basse-Kotto"),
    ("Mbomou", "Mbomou"),
    ("Haut-Mbomou", "Haut-Mbomou"),
    ("Vakaga", "Vakaga"),
    ("Bamingui-Bangoran", "Bamingui-Bangoran"),
    ("Nana-Grebizi", "Nana-Grebizi"),
    ("Ouham", "Ouham"),
    ("Ouham-Pende", "Ouham-Pende"),
    ("Lim-Pende", "Lim-Pende"),
    ("Haute-Kotto", "Haute-Kotto"),
    ("Kotto", "Kotto"),
    ("Mambéré", "Mambéré"),
]
prefecture = models.CharField(
    max_length=100,
    choices=PREFECTURES
)
class StructureSanitaire(models.Model):

    nom = models.CharField(max_length=200)

    prefecture = models.CharField(
    max_length=100,
    choices=PREFECTURES
)

    ville = models.CharField(
        max_length=150,
        blank=True
    )

    adresse = models.CharField(
        max_length=255,
        blank=True
    )

    telephone = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    latitude = models.FloatField(
        null=True,
        blank=True
    )

    longitude = models.FloatField(
        null=True,
        blank=True
    )

    photo = models.ImageField(
        upload_to='structures/',
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.nom
class Contact(models.Model):

    nom = models.CharField(max_length=200)

    email = models.EmailField()

    sujet = models.CharField(max_length=255)

    message = models.TextField()

    date_envoi = models.DateTimeField(
        auto_now_add=True
    )

    statut = models.CharField(
        max_length=30,
        default="Nouveau"
    )

    reponse = models.TextField(
        blank=True,
        null=True
    )

    transfert = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    archive = models.BooleanField(
        default=False
    )

    corbeille = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.sujet


class Notification(models.Model):

    utilisateur = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    titre = models.CharField(
        max_length=200
    )

    message = models.TextField()

    lu = models.BooleanField(
        default=False
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre
class Activite(models.Model):

    utilisateur = models.CharField(
        max_length=150
    )

    action = models.CharField(
        max_length=255
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.action

from django.contrib.auth.models import User

class Profil(models.Model):

    ROLES = (
        ("SUPERADMIN", "Super Administrateur"),
        ("ADMIN", "Administrateur"),
        ("AGENT", "Agent"),
    )

    utilisateur = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default="AGENT"
    )

    telephone = models.CharField(
        max_length=30,
        blank=True
    )

    photo = models.ImageField(
        upload_to="profils/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.utilisateur.username

class Gouvernance(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()

    organigramme_pdf = models.FileField(
        upload_to="organigrammes/",
        blank=True,
        null=True
    )

    image_organigramme = models.ImageField(
        upload_to="organigrammes/",
        blank=True,
        null=True
    )

    image_president = models.ImageField(
        upload_to="gouvernance/",
        blank=True,
        null=True
    )

    image_vice_president = models.ImageField(
        upload_to="gouvernance/",
        blank=True,
        null=True
    )

    image_directeur = models.ImageField(
        upload_to="gouvernance/",
        blank=True,
        null=True
    )

    date_creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def __str__(self):
        return self.titre
class Documentation(models.Model):

    titre=models.CharField(max_length=200)

    fichier=models.FileField(
        upload_to="documents/"
    )

    description=models.TextField(blank=True)

    date_creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
class Video(models.Model):

    titre=models.CharField(max_length=200)

    video=models.FileField(
        upload_to="videos/"
    )

    miniature=models.ImageField(
        upload_to="videos/",
        blank=True,
        null=True
    )

    description=models.TextField(blank=True)

    date_creation=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
class Apropos(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()

    historique = models.TextField(blank=True)

    mission = models.TextField(blank=True)

    vision = models.TextField(blank=True)

    valeurs = models.TextField(blank=True)

    objectifs = models.TextField(blank=True)

    engagement = models.TextField(blank=True)

    mot_president = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="apropos/",
        blank=True,
        null=True
    )

    logo = models.ImageField(
        upload_to="apropos/",
        blank=True,
        null=True
    )

    organigramme_image = models.ImageField(
        upload_to="organigramme/",
        blank=True,
        null=True
    )

    organigramme_pdf = models.FileField(
        upload_to="organigramme/",
        blank=True,
        null=True
    )

    organigramme_word = models.FileField(
        upload_to="organigramme/",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "À propos"
        verbose_name_plural = "À propos"

    def __str__(self):
        return self.titre

# ==========================
# GOUVERNANCE CONASAN
# ==========================

class Dirigeant(models.Model):
    nom = models.CharField(max_length=200)

    fonction = models.CharField(max_length=200)

    photo = models.ImageField(
        upload_to="gouvernance/",
        blank=True,
        null=True
    )

    biographie = models.TextField(blank=True)

    telephone = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField(blank=True)

    ordre = models.PositiveIntegerField(default=0)

    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return self.nom


class CODIS(models.Model):

    nom = models.CharField(max_length=150)

    responsable = models.CharField(max_length=200)

    photo = models.ImageField(
        upload_to="codis/",
        blank=True,
        null=True
    )

    nombre_fosa = models.PositiveIntegerField(default=0)

    equipe_mobile = models.PositiveIntegerField(default=0)

    adresse = models.CharField(
        max_length=250,
        blank=True
    )

    telephone = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField(blank=True)

    ordre = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["ordre"]

    def __str__(self):
        return self.nom


class DocumentOrganigramme(models.Model):

    titre = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="organigramme/",
        blank=True,
        null=True
    )

    pdf = models.FileField(
        upload_to="organigramme/",
        blank=True,
        null=True
    )

    word = models.FileField(
        upload_to="organigramme/",
        blank=True,
        null=True
    )

    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
from django.db import models


class GouvernanceDocument(models.Model):

    TYPE_CHOIX = [
        ("organigramme", "Organigramme"),
        ("decision", "Décision"),
        ("rapport", "Rapport"),
        ("proces_verbal", "Procès-verbal"),
        ("note_service", "Note de service"),
        ("autre", "Autre"),
    ]

    titre = models.CharField(
        max_length=250
    )

    type_document = models.CharField(
        max_length=30,
        choices=TYPE_CHOIX,
        default="organigramme"
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    fichier = models.FileField(
        upload_to="gouvernance/documents/"
    )

    image_apercu = models.ImageField(
        upload_to="gouvernance/apercus/",
        blank=True,
        null=True
    )

    publier = models.BooleanField(
        default=True
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    date_modification = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = "Document de gouvernance"
        verbose_name_plural = "Documents de gouvernance"

    def __str__(self):
        return self.titre
class Document(models.Model):

    CATEGORIES = [

        ("Rapport","Rapport"),

        ("Guide","Guide"),

        ("Procédure","Procédure"),

        ("Convention","Convention"),

        ("Formulaire","Formulaire"),

        ("Autre","Autre"),

    ]

    titre=models.CharField(
        max_length=255
    )

    categorie=models.CharField(
        max_length=100,
        choices=CATEGORIES,
        default="Autre"
    )

    description=models.TextField(
        blank=True
    )

    image=models.ImageField(
        upload_to="documents/images/",
        blank=True,
        null=True
    )

    fichier=models.FileField(
        upload_to="documents/fichiers/"
    )

    public=models.BooleanField(
        default=True
    )

    date_creation=models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.titre

class Galerie(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="galerie/"
    )

    categorie = models.CharField(
        max_length=100,
        default="Galerie"
    )

    publier = models.BooleanField(
        default=True
    )

    date_creation = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-date_creation"]
        verbose_name = "Photo"
        verbose_name_plural = "Galerie"

    def __str__(self):
        return self.titre
class Hero(models.Model):
    titre = models.CharField(max_length=255)
    sous_titre = models.TextField()

    image_fond = models.ImageField(upload_to="hero/")
    image_secondaire = models.ImageField(upload_to="hero/")

    verset = models.CharField(max_length=255, blank=True)
    reference = models.CharField(max_length=100, blank=True)

    texte_bouton1 = models.CharField(max_length=80, default="Découvrir nos actions")
    lien_bouton1 = models.CharField(max_length=200, default="/programmes/")

    texte_bouton2 = models.CharField(max_length=80, default="Nous contacter")
    lien_bouton2 = models.CharField(max_length=200, default="/contact/")

    publier = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Hero"

    def __str__(self):
        return self.titre
class HeroAccueil(models.Model):
    titre = models.CharField(max_length=100)
    image_fond = models.ImageField(upload_to="hero/")
    actif = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.actif:
            HeroAccueil.objects.exclude(pk=self.pk).update(actif=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre
class Video(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    miniature = models.ImageField(
        upload_to="videos/miniatures/",
        blank=True,
        null=True
    )
    video = models.FileField(upload_to="videos/")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
