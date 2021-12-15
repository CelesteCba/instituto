from django.db import models

# Create your models here.
class Oficina(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)

    class Meta:
        verbose_name='Oficina'
        verbose_name_plural='Oficinas del Instituto'
        ordering=['name']
    
    def __str__(self):
        return str(self.name)


class NoDocente(models.Model):

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    age= models.IntegerField("Edad")
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    avatar = models.ImageField('Imagen', upload_to= 'registro', height_field=None, width_field=None, max_length=None, blank=True)

    

    class Meta:
        """Meta definition for NoDocente."""

        verbose_name = 'No Docente'
        verbose_name_plural = 'No Docentes'

    def __str__(self):
        return self.last_name + ', ' + self.first_name
        

class Materia(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)
    

    class Meta:
        """Meta definition for Materia."""

        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        return str(self.name)



class Docente(models.Model):

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    age=models.IntegerField("Edad")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    avatar = models.ImageField('Imagen', upload_to= 'registro', height_field=None, width_field=None, max_length=None, blank=True)


    class Meta:
        """Meta definition for Docente."""

        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'

    def __str__(self):
        return self.last_name + ', ' + self.first_name
