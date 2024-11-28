from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator #para hacer validaciones especiales letras y espacio (o expresiones regulares)
from datetime import date
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

def validar_fecha_vencimiento(fecha_elaboracion, fecha_vencimiento):
    if fecha_elaboracion is None or fecha_vencimiento is None:
        raise ValidationError("Ambas fechas (elaboración y vencimiento) son obligatorias.")

    if fecha_vencimiento <= fecha_elaboracion:
        raise ValidationError("La fecha de vencimiento debe ser posterior a la fecha de elaboración.")

    fecha_limite = fecha_elaboracion + relativedelta(years=5)
    if fecha_vencimiento > fecha_limite:
        raise ValidationError("La fecha de vencimiento no puede ser más de 5 años después de la fecha de elaboración.")