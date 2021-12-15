# Generated by Django 3.2.8 on 2021-11-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20211129_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='materia',
            name='short_name',
            field=models.CharField(max_length=50, verbose_name='Nombre corto'),
        ),
        migrations.AlterField(
            model_name='nodocente',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='nodocente',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='short_name',
            field=models.CharField(max_length=50, verbose_name='Nombre corto'),
        ),
    ]
