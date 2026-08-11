# ===============================
# GOUVERNANCE
# ===============================

from django import forms

from .models import (
    Dirigeant,
    CODIS,
    DocumentOrganigramme
)


class DirigeantForm(forms.ModelForm):

    class Meta:

        model = Dirigeant

        fields = "__all__"

        widgets = {

            "nom": forms.TextInput(attrs={"class":"form-control"}),

            "fonction": forms.TextInput(attrs={"class":"form-control"}),

            "telephone": forms.TextInput(attrs={"class":"form-control"}),

            "email": forms.EmailInput(attrs={"class":"form-control"}),

            "ordre": forms.NumberInput(attrs={"class":"form-control"}),

            "biographie": forms.Textarea(attrs={
                "class":"form-control",
                "rows":6
            }),

            "actif": forms.CheckboxInput()

        }


class CODISForm(forms.ModelForm):

    class Meta:

        model = CODIS

        fields = "__all__"

        widgets = {

            "nom": forms.TextInput(attrs={"class":"form-control"}),

            "responsable": forms.TextInput(attrs={"class":"form-control"}),

            "adresse": forms.TextInput(attrs={"class":"form-control"}),

            "telephone": forms.TextInput(attrs={"class":"form-control"}),

            "email": forms.EmailInput(attrs={"class":"form-control"}),

            "nombre_fosa": forms.NumberInput(attrs={"class":"form-control"}),

            "equipe_mobile": forms.NumberInput(attrs={"class":"form-control"}),

            "ordre": forms.NumberInput(attrs={"class":"form-control"}),

        }


class DocumentOrganigrammeForm(forms.ModelForm):

    class Meta:

        model = DocumentOrganigramme

        fields = "__all__"

        widgets = {

            "titre": forms.TextInput(attrs={"class":"form-control"}),

        }

from django import forms
from .models import Galerie


class GalerieForm(forms.ModelForm):

    class Meta:

        model = Galerie

        fields = [
            "titre",
            "description",
            "categorie",
            "image",
            "publier",
        ]

        widgets = {

            "titre": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "description": forms.Textarea(attrs={
                "class":"form-control",
                "rows":4
            }),

            "categorie": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "image": forms.ClearableFileInput(attrs={
                "class":"form-control"
            }),

            "publier": forms.CheckboxInput(attrs={
                "class":"form-check-input"
            })

        }
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = "__all__"
from django import forms
from .models import GouvernanceDocument


class GouvernanceDocumentForm(forms.ModelForm):

    class Meta:
        model = GouvernanceDocument

        fields = [
            "titre",
            "type_document",
            "description",
            "fichier",
            "image_apercu",
            "publier",
        ]

        widgets = {
            "titre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Titre du document"
            }),

            "type_document": forms.Select(attrs={
                "class": "form-select"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Description du document"
            }),

            "fichier": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "image_apercu": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "publier": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }
