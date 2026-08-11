from django.contrib import admin

from .models import (
    Programme,
    Actualite,
    Partenaire,
    StructureSanitaire,
    Contact,
    Notification,
    Profil,
    Gouvernance,
    Apropos,
    Documentation,
    Galerie,
    Video,
    GouvernanceDocument,
    Document,
)


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'date_creation'
    )

    search_fields = (
        'titre',
    )


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'date_publication'
    )

    search_fields = (
        'titre',
    )


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
    )

    search_fields = (
        'nom',
    )


@admin.register(StructureSanitaire)
class StructureAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'adresse',
        'telephone',
        'email'
    )

    search_fields = (
        'nom',
        'adresse',
        'telephone',
        'email'
    )
    list_filter = (
    'prefecture',
)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'utilisateur',
        'lu',
        'date_creation'
    )

    list_filter = (
        'lu',
        'date_creation'
    )
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'email',
        'sujet',
        'statut',
        'date_envoi'
    )

    list_filter = (
        'statut',
        'archive',
        'corbeille'
    )

    search_fields = (
        'nom',
        'email',
        'sujet'
    )

    actions = [
        'marquer_lu',
        'archiver_messages',
        'mettre_corbeille'
    ]

    def marquer_lu(self, request, queryset):
        queryset.update(statut="Lu")

    marquer_lu.short_description = "Marquer comme lu"

    def archiver_messages(self, request, queryset):
        queryset.update(archive=True)

    archiver_messages.short_description = "Archiver"

    def mettre_corbeille(self, request, queryset):
        queryset.update(corbeille=True)

    mettre_corbeille.short_description = "Mettre à la corbeille"
@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):

    list_display = (
        "utilisateur",
        "role",
        "telephone",
    )

    list_filter = (
        "role",
    )

    search_fields = (
        "utilisateur__username",
        "utilisateur__first_name",
        "utilisateur__last_name",
    )

@admin.register(Gouvernance)
class GouvernanceAdmin(admin.ModelAdmin):
    list_display=("titre","date_creation")


@admin.register(Apropos)
class AproposAdmin(admin.ModelAdmin):
    list_display=("titre",)


@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    list_display=("titre","date_creation")

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("titre", "date")
    search_fields = ("titre",)
    list_filter = ("date",)
@admin.register(GouvernanceDocument)
class GouvernanceDocumentAdmin(admin.ModelAdmin):

    list_display = (
        "titre",
        "type_document",
        "publier",
        "date_creation",
    )

    list_filter = (
        "type_document",
        "publier",
    )

    search_fields = (
        "titre",
        "description",
    )
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):

    list_display=(

        "titre",

        "categorie",

        "public",

        "date_creation"

    )

    list_filter=(

        "categorie",

        "public"

    )

    search_fields=(

        "titre",

        "description"

    )

@admin.register(Galerie)
class GalerieAdmin(admin.ModelAdmin):

    list_display = (
        "titre",
        "categorie",
        "publier",
        "date_creation",
    )

    list_filter = (
        "categorie",
        "publier",
    )

    search_fields = (
        "titre",
    )
from .models import HeroAccueil

@admin.register(HeroAccueil)
class HeroAccueilAdmin(admin.ModelAdmin):
    list_display = ("titre", "actif")
