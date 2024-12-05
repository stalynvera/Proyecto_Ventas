from rest_framework import serializers
from .models import Clientes, Productos, Empleados, Empresas, Proveedores, Factura, MetodoPago,Descuento,Venta,DetalleVenta,Envio,Pago

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes  # Asegúrate de que este es el nombre correcto de tu modelo
        fields = '__all__'

class ProductosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos  # Especifica el modelo relacionado
        fields = '__all__'

class EmpleadosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'
class EmpresasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = '__all__'
class proveedoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
class FacturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class MetodoPagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'

class DescuentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Descuento
        fields = '__all__'

class VentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'
        
class DetalleVentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = '__all__'

class EnvioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'

class PagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'
        