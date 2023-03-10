# Generated by Django 4.1.3 on 2023-01-31 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_rename_products_trainers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainers',
            old_name='free',
            new_name='is_free',
        ),
        migrations.AddField(
            model_name='trainers',
            name='email',
            field=models.EmailField(default='prueba@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainers',
            name='phone_number',
            field=models.CharField(default='Numero Inexistente', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainers',
            name='teches',
            field=models.CharField(choices=[('Funcional', 'Funcional'), ('Spinning', 'Spinning'), ('Crossfit', 'Crossfit'), ('Arte-Marcial', 'Arte-Marcial')], default='Funcional', max_length=50),
            preserve_default=False,
        ),
    ]
