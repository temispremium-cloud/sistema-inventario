# Sistema de Inventario Multialmacén

Proyecto Django del Grupo 1 (Programación Avanzada, Uniguajira). Sistema para controlar los productos que ingresan y salen de las bodegas de una empresa con varios almacenes. Registra artículos, lotes, la ubicación de cada lote (almacén y estante) y cada movimiento de entrada o salida. Toda la información se gestiona desde el panel de administración de Django.

## Integrantes

- Temistocle
- Alain
- Andrés

## Actores

- Administrador
- Jefe de bodega
- Bodeguero

## Estructura

Cada tabla del diagrama ER es un modelo en su propia app:

| App | Modelo | Descripción |
|---|---|---|
| almacenes | Almacen | Bodegas de la empresa |
| ubicaciones | Ubicacion | Estantes de cada almacén (entidad débil) |
| categorias | Categoria | Categorías de artículos |
| articulos | Articulo | Productos del inventario |
| lotes | Lote | Lotes de cada artículo (entidad débil) |
| movimientos | Movimiento | Entradas y salidas |
| detalles_movimiento | DetalleMovimiento | Tabla intermedia del N:M entre Movimiento y Lote (cantidad) |

El stock no es una columna: se calcula sumando las entradas y restando las salidas registradas en DetalleMovimiento.

## Cómo ejecutarlo

1. Clonar el repositorio y entrar a la carpeta:

        git clone URL_DEL_REPOSITORIO
        cd sistema-inventario

2. Crear y activar el entorno virtual (Windows PowerShell):

        py -m venv venv
        venv\Scripts\Activate.ps1

3. Instalar dependencias:

        python -m pip install -r requirements.txt

4. Aplicar migraciones (la base db.sqlite3 ya incluye datos de prueba):

        python manage.py migrate

5. Iniciar el servidor:

        python manage.py runserver

6. Abrir http://127.0.0.1:8000/admin/

## Credenciales del administrador

- Usuario: admin
- Contraseña: Inventario2026

## Diagramas

En la carpeta docs/:

- diagrama_actores.png (casos de uso)
- diagrama_er.png (entidad-relación)