from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientesSerializers,ProductosSerializers,EmpleadosSerializers,EmpresasSerializers,proveedoresSerializers,facturaDeserializers
from .models import Clientes, Productos, Empleados, Empresas, Proveedores, Factura

class ClientesViewSet(viewsets.ModelViewSet):
     queryset = Clientes.objects.all()
     serializer_class = ClientesSerializers

class ProductosViewSet(viewsets.ModelViewSet):
     queryset = Productos.objects.all()
     serializer_class = ProductosSerializers

class EmpleadosViewSet(viewsets.ModelViewSet):
     queryset = Empleados.objects.all()
     serializer_class = EmpleadosSerializers

class EmpresasViewSet(viewsets.ModelViewSet):
     queryset = Empresas.objects.all()
     serializer_class = EmpresasSerializers

class ProveedoresViewSet(viewsets.ModelViewSet):
     queryset = Proveedores.objects.all()
     serializer_class = proveedoresSerializers

class FacturaViewSet(viewsets.ModelViewSet):
     queryset = Factura.objects.all()
     serializer_class = facturaDeserializers


