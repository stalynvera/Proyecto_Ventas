"""
URL configuration for Sis_ven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ventasapp.views import ClientesViewSet, ProductosViewSet, EmpleadosViewSet, EmpresasViewSet, ProveedoresViewSet, FacturaViewSet,MetodoPagoViewSet, DescuentoViewSet, VentaViewSet,DetalleVentaViewSet,EnvioViewSet,PagoViewSet
from rest_framework.routers import DefaultRouter

# Crear el router y registrar los ViewSets
rutas = DefaultRouter()
rutas.register('Empresas', EmpresasViewSet)
rutas.register('Proveedores', ProveedoresViewSet)
rutas.register('Productos', ProductosViewSet)
rutas.register('Empleados', EmpleadosViewSet)
rutas.register('Clientes', ClientesViewSet)
rutas.register('Descuento', DescuentoViewSet)
rutas.register('Venta', VentaViewSet)
rutas.register('DetalleVenta', DetalleVentaViewSet)
rutas.register('Factura', FacturaViewSet)
rutas.register('MetodoPago', MetodoPagoViewSet)
rutas.register('Pago', PagoViewSet)
rutas.register('Envio', EnvioViewSet)

# Rutas de la API
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rutas.urls)),  # Incluir las rutas de la API
]

