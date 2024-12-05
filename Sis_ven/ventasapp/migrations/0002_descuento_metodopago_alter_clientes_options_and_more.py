# Generated by Django 5.1.3 on 2024-12-05 13:34

import django.core.validators
import django.db.models.deletion
import ventasapp.validadores
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventasapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del descuento')),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción del descuento')),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Descuento',
                'verbose_name_plural': 'Descuentos',
                'db_table': 'Descuentos',
            },
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de Crédito/Débito'), ('transferencia', 'Transferencia Bancaria')], default='efectivo', max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Método de Pago',
                'verbose_name_plural': 'Métodos de Pago',
                'db_table': 'MetodoPago',
            },
        ),
        migrations.AlterModelOptions(
            name='clientes',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelOptions(
            name='proveedores',
            options={'verbose_name': 'Proveedor', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.RenameField(
            model_name='clientes',
            old_name='Fecha_nacimiento',
            new_name='fecha_nacimiento',
        ),
        migrations.RenameField(
            model_name='factura',
            old_name='total',
            new_name='total_factura',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='cedula',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, validators=[ventasapp.validadores.validacion_numeros, django.core.validators.MinLengthValidator(10), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[ventasapp.validadores.validar_email]),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=10, validators=[ventasapp.validadores.validar_telefono]),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_factura',
            field=models.DateTimeField(auto_now_add=True, validators=[ventasapp.validadores.validar_fecha_factura]),
        ),
        migrations.AlterField(
            model_name='productos',
            name='cantidad_stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad en stock : '),
        ),
        migrations.AlterField(
            model_name='productos',
            name='codigo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, validators=[ventasapp.validadores.validacion_numeros, django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='productos',
            name='nombre',
            field=models.CharField(max_length=50, validators=[ventasapp.validadores.Validacion_letras], verbose_name='Nombre del producto : '),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, help_text='Ingresa valores con decimales', max_digits=10, validators=[ventasapp.validadores.validar_precio], verbose_name='Precio del producto : '),
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.clientes')),
                ('descuento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ventasapp.descuento')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.empleados')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.metodopago')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.metodopago')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.venta')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
                'db_table': 'Pagos',
            },
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_envio', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('estado_envio', models.CharField(choices=[('pendiente', 'Pendiente'), ('enviado', 'Enviado'), ('entregado', 'Entregado')], default='pendiente', max_length=20)),
                ('fecha_entrega_estimada', models.DateTimeField()),
                ('venta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.venta')),
            ],
            options={
                'verbose_name': 'Envio',
                'verbose_name_plural': 'Envios',
                'db_table': 'Envios',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.productos')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventasapp.venta')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalles de Venta',
                'db_table': 'DetalleVenta',
            },
        ),
        migrations.AddField(
            model_name='factura',
            name='venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ventasapp.venta'),
        ),
    ]
