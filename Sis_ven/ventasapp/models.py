from datetime import date
from django.db import models
from django.forms import ValidationError
from .choices import CATEGORIAS
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from .validadores import validacion_numeros, Validacion_letras, validacion_especial3, validar_fecha_nacimiento, validar_fecha_vencimiento, validar_email, validar_telefono, validar_precio, validar_stock, validar_fecha_factura,validacion_especial

# Create your models here.
class Clientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators=[validacion_numeros, MinLengthValidator(10), MaxLengthValidator(10)])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del cliente : ', validators=[Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False, validators=[Validacion_letras])
    telefono = models.CharField(max_length=10, validators=[validar_telefono])
    email = models.EmailField(unique=True, validators=[validar_email])
    direccion = models.TextField(validators=[validacion_especial3])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])  # Cambié 'Fecha_nacimiento' por 'fecha_nacimiento'

    def __str__(self):
        return f"{self.nombre} {self.apellido} "

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'


class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True, validators=[MaxLengthValidator(10),validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name=' Nombre del producto : ', validators=[Validacion_letras]) 
    marca = models.CharField(max_length=50, unique=True, validators=[Validacion_letras])
    caracteristicas_categoria = models.CharField(max_length=100, choices=CATEGORIAS, validators=[validacion_especial3])
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='ingresa valores con decimales', verbose_name='Precio del producto : ', validators=[validacion_numeros])
    cantidad_stock = models.IntegerField(verbose_name='Cantidad en stock : ', validators=[validacion_numeros])
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    
    # Cambié esto para que sea un valor 'date' en lugar de una cadena
    fecha_elaboracion = models.DateField(blank=True)
    fecha_vencimiento = models.DateField(default=date(2024, 1, 1))  # Corregido para ser un objeto de tipo 'date'
    
    def clean(self):
        # Llamar al validador de fechas dentro del método clean()
        validar_fecha_vencimiento(self.fecha_elaboracion, self.fecha_vencimiento)

    def actualizar_stock(self, cantidad):
        self.cantidad_stock -= cantidad  # Actualiza el stock al restar la cantidad
        self.save()

    def __str__(self):
        return f"{self.nombre}  {self.marca} "
    
    class Meta:
        verbose_name = 'Producto :'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'

class Empresas(models.Model):
    ruc = models.CharField(primary_key=True, max_length=13, unique=True, validators=[validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre de la empresa : ', validators=[Validacion_letras])
    direccion = models.TextField(validators=[validacion_especial3])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True, validators=[validacion_especial3])

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = 'Empresa :'
        verbose_name_plural = 'Empresas'
        db_table = 'Empresas'


class Proveedores(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators=[MaxLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del proveedor : ', validators=[Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False, validators=[Validacion_letras])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True, validators=[validacion_especial3])
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedores'


class Empleados(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, verbose_name='Cedula del Empleado :', validators=[validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del Empleado : ', validators=[Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False, validators=[Validacion_letras])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True, validators=[validacion_especial3])
    direccion = models.TextField(validators=[validacion_especial3])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'


class MetodoPago(models.Model):
    tipo = models.CharField(max_length=50, choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de Crédito/Débito'), ('transferencia', 'Transferencia Bancaria')], default='efectivo')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo}"

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'
        db_table = 'MetodoPago'


class Descuento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del descuento")
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción del descuento")
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def esta_activo(self):
        """Verifica si el descuento está activo en la fecha actual"""
        from django.utils import timezone
        ahora = timezone.now()
        return self.fecha_inicio <= ahora <= self.fecha_fin

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
        db_table = 'Descuentos'


class Venta(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuento, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def calcular_total(self):
        """Calcula el total de la venta, aplicando el descuento si corresponde."""
        total = sum(detalle.subtotal() for detalle in self.detalleventa_set.all())
        if self.descuento and self.descuento.esta_activo():
            descuento_valido = total * (self.descuento.porcentaje / Decimal(100))
            total -= descuento_valido
        self.total = total
        self.save()

    def __str__(self):
        return f"Venta #{self.id} - Cliente: {self.cliente.nombre}"

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Ventas'


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        """Calcula el subtotal de este detalle de venta (precio * cantidad)."""
        return self.precio_unitario * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad}"

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        db_table = 'DetalleVenta'


class Envio(models.Model):
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    direccion_envio = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado_envio = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('entregado', 'Entregado')],
        default='pendiente'
    )
    fecha_entrega_estimada = models.DateTimeField()

    def __str__(self):
        return f"Envío #{self.id} - Venta #{self.venta.id}"

    class Meta:
        verbose_name = 'Envio'
        verbose_name_plural = 'Envios'
        db_table = 'Envios'


class Pago(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de ${self.monto} para la venta #{self.venta.id}"

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        db_table = 'Pagos'


class Factura(models.Model):
    codigo_factura = models.AutoField(primary_key=True)
    fecha_factura = models.DateTimeField(auto_now_add=True, validators=[validar_fecha_factura])
    cliente = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleados', on_delete=models.CASCADE)
    venta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=True)  # Cambié a null=True
    iva = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def calcular_factura(self):
        """Calcula el IVA y el total de la factura basado en la venta."""
        self.iva = self.venta.total * Decimal(0.15) if self.venta else Decimal(0)
        self.total_factura = self.venta.total + self.iva if self.venta else Decimal(0)
        self.save()

    def __str__(self):
        return f"Factura {self.codigo_factura} - Cliente: {self.cliente.nombre} - Total: ${self.total_factura}"

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        db_table = 'Facturas'
