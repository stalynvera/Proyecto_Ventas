from django.contrib import admin
from .models import Clientes, Empleados, Factura, Productos, Proveedores, Empresas, Venta, MetodoPago, Descuento, DetalleVenta, Envio, Pago

# Registro del modelo Clientes en el panel de administración
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'direccion', 'email')
    search_fields = ('cedula', 'nombre', 'apellido')
    list_filter = ('cedula', 'apellido')

# Registro del modelo Empleados en el panel de administración
@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'telefono', 'email', 'direccion', 'fecha_creacion', 'fecha_nacimiento')
    search_fields = ('cedula', 'apellido')

# Registro del modelo Productos en el panel de administración
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio', 'cantidad_stock', 'fecha_ingreso', 'fecha_vencimiento')
    search_fields = ('nombre', 'marca', 'codigo')
    list_filter = ('caracteristicas_categoria', 'fecha_vencimiento')  # Cambié 'categoria' por 'caracteristicas_categoria'

# Registro del modelo Factura en el panel de administración
@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('codigo_factura', 'fecha_factura', 'cliente', 'empleado', 'iva', 'total_factura')
    search_fields = ('codigo_factura', 'cliente__nombre', 'empleado__nombre')
    list_filter = ('fecha_factura', 'cliente', 'empleado')

    def productos(self, obj):
        """Muestra los productos relacionados a través de la venta"""
        return ', '.join([detalle.producto.nombre for detalle in obj.venta.detalleventa_set.all()])
    productos.short_description = 'Productos'

    def cantidad_total(self, obj):
        """Muestra la cantidad total de productos en la venta"""
        return sum([detalle.cantidad for detalle in obj.venta.detalleventa_set.all()])
    cantidad_total.short_description = 'Cantidad Total'

    def total_factura(self, obj):
        """Devuelve el total calculado de la factura"""
        return obj.total_factura
    total_factura.short_description = 'Total de la Factura'

    def cliente(self, obj):
        """Devuelve el nombre del cliente"""
        return obj.cliente.nombre
    cliente.short_description = 'Cliente'

    def empleado(self, obj):
        """Devuelve el nombre del empleado"""
        return obj.empleado.nombre
    empleado.short_description = 'Empleado'

# Registro del modelo Proveedores en el panel de administración
@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'empresa')  # Añadido 'empresa' para mostrar la relación con Empresas
    search_fields = ('cedula', 'nombre', 'apellido')

# Registro del modelo Empresas en el panel de administración
@admin.register(Empresas)
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'nombre', 'telefono', 'direccion')  # Añadido 'direccion' para completar la visualización
    search_fields = ('ruc', 'nombre')

# Registro de los modelos adicionales que no se habían registrado
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'empleado', 'metodo_pago', 'fecha_venta', 'total')
    search_fields = ('cliente__nombre', 'empleado__nombre', 'metodo_pago__tipo')
    list_filter = ('fecha_venta', 'metodo_pago', 'empleado')

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descripcion')
    search_fields = ('tipo',)

@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porcentaje', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre',)

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('producto__nombre',)

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = ('venta', 'direccion_envio', 'estado_envio', 'fecha_envio', 'fecha_entrega_estimada')
    search_fields = ('venta__cliente__nombre',)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('venta', 'monto', 'metodo_pago', 'fecha_pago')
    search_fields = ('venta__cliente__nombre', 'monto')

