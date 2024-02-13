from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from PensionAnimal.models.Personne import Personne


# Register your models here.
@admin.register(Personne)
class BlogPostAdmin(ImportExportModelAdmin):
    pass