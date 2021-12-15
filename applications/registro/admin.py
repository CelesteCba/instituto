from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Oficina)
admin.site.register(Materia)  

class DocenteAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name',
        'materia',
        'id',
    )
    search_fields=('last_name', 'first_name')


admin.site.register(Docente,DocenteAdmin) 
class NoDocenteAdmin(admin.ModelAdmin):
    list_display=(
        'last_name',
        'first_name',
        'oficina',
        'id',
    )
    search_fields=('last_name', 'first_name')

admin.site.register(NoDocente,NoDocenteAdmin)
