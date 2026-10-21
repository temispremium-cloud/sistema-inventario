from django.db import models


class Lote(models.Model):
    articulo = models.ForeignKey("articulos.Articulo", on_delete=models.CASCADE, related_name="lotes")
    ubicacion = models.ForeignKey("ubicaciones.Ubicacion", on_delete=models.PROTECT, related_name="lotes")
    codigo = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Lote {self.codigo} ({self.articulo.nombre})"
