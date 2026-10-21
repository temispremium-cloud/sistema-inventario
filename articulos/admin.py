from django.contrib import admin

from lotes.models import Lote
from .models import Articulo


class LoteInline(admin.TabularInline):
    model = Lote
    extra = 1


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("codigo", "nombre", "categoria", "unidad")
    search_fields = ("codigo", "nombre")
    list_filter = ("categoria", "unidad")
    inlines = [LoteInline]
