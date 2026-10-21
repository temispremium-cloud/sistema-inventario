from django.contrib import admin

from .models import DetalleMovimiento


class DetalleMovimientoInline(admin.TabularInline):
    model = DetalleMovimiento
    extra = 1


@admin.register(DetalleMovimiento)
class DetalleMovimientoAdmin(admin.ModelAdmin):
    list_display = ("movimiento", "lote", "cantidad")
    search_fields = ("lote__codigo",)
    list_filter = ("movimiento__tipo",)
