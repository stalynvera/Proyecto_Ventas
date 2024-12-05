import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #para hacer validaciones especiales letras y espacio (o expresiones regulares)
from datetime import date
import re
from dateutil.relativedelta import relativedelta
def validacion_numeros(value):
    if isinstance(value, str):
      if not value.isdigit():
        raise ValidationError("El valor debe contener solo números") #raise funciona como como un print para devolver un mensajhe en caso de que no se cumpla la condicion
    
def Validacion_letras(value):
    if not value.isalpha():
        raise ValidationError("El valor debe contener solo letras")

 #expresiones regulares
   
validacion_especial = RegexValidator(
    regex= r'^[a-zA-Z\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'

)

#validacion numeros letras y espacios
validacion_especial2 = RegexValidator(
    regex= r'^[a-zA-Z0-9\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'

)

#validacion numeros, letras y espacios y caracteres especiales
validacion_especial3 = RegexValidator(
    regex= r'^[a-zA-Z0-9,-ó\s]+$', #para establecer la expresion regular o cadena permitidos 
    message= 'el campo solo debe contener letras y espacios'
)

def validar_fecha_nacimiento(value):
    hoy = date.today()
    edad_maxima = 60
    fecha_limite = date(hoy.year - edad_maxima, hoy.month, hoy.day)
    if value < fecha_limite:
        raise ValidationError(f"La fecha de nacimiento no puede indicar más de {edad_maxima} años de antigüedad.")

from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

def validar_fecha_vencimiento(fecha_elaboracion, fecha_vencimiento):
    if fecha_elaboracion is None or fecha_vencimiento is None:
        raise ValidationError("Ambas fechas (elaboración y vencimiento) son obligatorias.")
    
    # Asegurarse de que las fechas son del tipo correcto
    if not isinstance(fecha_elaboracion, (date, datetime)) or not isinstance(fecha_vencimiento, (date, datetime)):
        raise ValidationError("Las fechas deben ser objetos de tipo 'date' o 'datetime'.")
    
    # Validar que la fecha de vencimiento es posterior a la fecha de elaboración
    if fecha_vencimiento <= fecha_elaboracion:
        raise ValidationError("La fecha de vencimiento debe ser posterior a la fecha de elaboración.")
    
    # Verificar que la fecha de vencimiento no sea más de 5 años posterior a la fecha de elaboración
    fecha_limite = fecha_elaboracion + relativedelta(years=5)
    if fecha_vencimiento > fecha_limite:
        raise ValidationError("La fecha de vencimiento no puede ser más de 5 años después de la fecha de elaboración.")
def validar_email(value):
    """Valida que el correo electrónico tenga un formato correcto."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, value):
        raise ValidationError("El correo electrónico no tiene un formato válido.")
def validar_telefono(value):
    """Valida que el número de teléfono tenga exactamente 10 dígitos numéricos."""
    if len(value) != 10 or not value.isdigit():
        raise ValidationError("El número de teléfono debe contener exactamente 10 dígitos.")
def validar_precio(value):
    """Valida que el precio no sea negativo."""
    if value < 0:
        raise ValidationError("El precio no puede ser negativo.")
def validar_stock(producto, cantidad):
    """Valida que el stock sea suficiente para la venta."""
    if cantidad > producto.cantidad_stock:
        raise ValidationError(f"No hay suficiente stock para el producto {producto.nombre}. Solo quedan {producto.cantidad_stock} unidades.")
def validar_fecha_factura(value):
    """Valida que la fecha de la factura no sea en el futuro."""
    if value > date.today():
        raise ValidationError("La fecha de la factura no puede ser en el futuro.")
