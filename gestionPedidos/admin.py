from django.contrib import admin

from gestionPedidos.models import Clientes, Pedidos, Articulos

class clientesAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','email','telefono')
    search_fields=('nombre','telefono')

class pedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha','entregado')
    search_fields=('numero','fecha')
    list_filter=('fecha',)
    date_hierarchy='fecha'

class articulosAdmin(admin.ModelAdmin):
    list_display=('nombre','seccion','precio')
    search_fields=('nombre','seccion')
    list_filter=('seccion',)

admin.site.register(Clientes,clientesAdmin)
admin.site.register(Pedidos, pedidosAdmin)
admin.site.register(Articulos, articulosAdmin)