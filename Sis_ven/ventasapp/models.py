from django.db import models
from .choices import CATEGORIAS
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from .validadores import validacion_numeros, Validacion_letras, validacion_especial,validacion_especial2,validacion_especial3, validar_fecha_nacimiento, validar_fecha_vencimiento

# Create your models here.
class Clientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators= [MaxLengthValidator(10), validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name= 'Nombre del cliente : ', validators=[Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False,validators=[Validacion_letras])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True,validators=[validacion_especial3])
    direccion = models.TextField(validators=[validacion_especial3])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    Fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])

    def __str__(self):
        return f"{self.nombre} {self.apellido} "
    class Meta:
        verbose_name = 'ingresa los datos del Cliente :'
        verbose_name_plural = 'datos Clientes'
        db_table = 'Clientes'


class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True, validators=[MaxLengthValidator(10),validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name=' Nombre del producto : ', validators=[Validacion_letras]) 
    marca = models.CharField(max_length=50, unique=True, validators=[Validacion_letras])
    caracteristicas_categoria = models.CharField(max_length=100, choices= CATEGORIAS, validators=[validacion_especial3])
    precio = models.DecimalField(max_digits=10, decimal_places=2, help_text='ingresa valores con decimales', verbose_name='Precio del producto : ', validators=[validacion_numeros])
    cantidad_stock = models.IntegerField(verbose_name='Cantidad en stock : ', validators=[validacion_numeros])
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_elaboracion = models.DateField(blank=True)
    fecha_vencimiento = models.DateField(default='2024-01-01')
    
    def clean(self):
        validar_fecha_vencimiento(self.fecha_elaboracion,self.fecha_vencimiento)


    def actualizar_stock (self, cantidad):
        self.cantidad_stock -= cantidad # -= es una forma de operar (parecido a los contadores) siempre y cuadno sea una sola operacion contador = contador + 1
        self.save()

    def __str__(self):
        return f"{self.nombre}  {self.marca} "
    class Meta:
        verbose_name = 'Producto :'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'

class Empresas (models.Model):
    ruc = models.CharField(primary_key=True, max_length=13, unique=True, validators=[validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre de la empresa : ', validators=[Validacion_letras])
    direccion = models.TextField(validators=[validacion_especial3])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True, validators=[validacion_especial3])

    def __str__(self):
        return f"{self.nombre} "
    class Meta:
        verbose_name = 'Empresa :'
        verbose_name_plural = 'Empresas'
        db_table = 'Empresas'

class Proveedores (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, validators=[MaxLengthValidator(10),validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del proveedor : ', validators=[Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False, validators=[Validacion_letras])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True, validators=[validacion_especial3])
    empresa = models.ForeignKey(Empresas, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.nombre} ' ' {self.apellido} "
    class Meta:
        verbose_name = 'Proveedor '
        verbose_name_plural = 'Proveedores'
        db_table = 'Proveedores'

class Empleados (models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True, verbose_name= 'Cedula del Empleado :', validators=[validacion_numeros])
    nombre = models.CharField(max_length=50, blank=False, verbose_name='Nombre del Empleado : ', validators=[Validacion_letras])
    apellido = models.CharField(max_length=50, blank=False, validators=[Validacion_letras])
    telefono = models.CharField(max_length=10, validators=[validacion_numeros])
    email = models.EmailField(unique=True, validators=[validacion_especial3])
    direccion = models.TextField(validators=[validacion_especial3])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])


    def __str__(self):
        return f"{self.nombre} ' ' {self.apellido} "
    class Meta:
        verbose_name = 'Empleado :'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'

class Factura(models.Model):
    codigo_factura = models.AutoField(primary_key=True)
    fecha_factura = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=True, default=0)
    iva = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

        
    def save(self, *args, **kwargs):
        """Sobrescribe el método save para calcular valores automáticamente."""
        self.subtotal = self.cantidad * self.producto.precio
        self.iva = self.subtotal * Decimal(0.15)
        self.total = self.subtotal + self.iva
        self.producto.cantidad_stock = int(self.producto.cantidad_stock) - int(self.cantidad)
        self.producto.actualizar_stock(self.cantidad)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.codigo_factura} - Cliente: {self.cliente.nombre} - Total: ${self.total}"

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        db_table = 'Facturas'