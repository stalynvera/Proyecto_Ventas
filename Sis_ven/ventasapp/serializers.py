from rest_framework import serializers
from .models import Clientes, Productos, Empleados, Empresas, Proveedores, Factura

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
class facturaDeserializers(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'