# Generated by Django 3.2.8 on 2021-12-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0004_auto_20211129_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='registro', verbose_name='Imagen'),
        ),
    ]
