from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientesSerializers,ProductosSerializers,EmpleadosSerializers,EmpresasSerializers,proveedoresSerializers,MetodoPagoSerializers,DescuentoSerializers,VentaSerializers,DetalleVentaSerializers,EnvioSerializers,PagoSerializers,FacturaSerializers
from .models import Clientes, Productos, Empleados, Empresas, Proveedores, Factura,MetodoPago,Descuento,Venta,DetalleVenta,Envio,Pago

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
     serializer_class = FacturaSerializers

class MetodoPagoViewSet(viewsets.ModelViewSet):
     queryset = MetodoPago.objects.all()
     serializer_class = MetodoPagoSerializers

class DescuentoViewSet(viewsets.ModelViewSet):
     queryset = Descuento.objects.all()
     serializer_class = DescuentoSerializers

class VentaViewSet(viewsets.ModelViewSet):
     queryset = Venta.objects.all()
     serializer_class = VentaSerializers

class DetalleVentaViewSet(viewsets.ModelViewSet):
     queryset = DetalleVenta.objects.all()
     serializer_class = DetalleVentaSerializers

class EnvioViewSet(viewsets.ModelViewSet):
     queryset = Envio.objects.all()
     serializer_class = EnvioSerializers

class PagoViewSet(viewsets.ModelViewSet):
     queryset = Pago.objects.all()
     serializer_class = PagoSerializers




