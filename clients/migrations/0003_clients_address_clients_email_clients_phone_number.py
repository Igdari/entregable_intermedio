# Generated by Django 4.1.3 on 2023-01-31 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_rename_products_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='address',
            field=models.CharField(default='Valor Nulo', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='email',
            field=models.EmailField(default='prueba@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clients',
            name='phone_number',
            field=models.CharField(default='Numero inexistente', max_length=20),
            preserve_default=False,
        ),
    ]
