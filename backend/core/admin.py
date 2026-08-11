from django.contrib import admin
from .models import Programme
@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):

    list_display = (
        "titre",
    )

# Register your models here.
