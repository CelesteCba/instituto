from django import forms
from .models import Docente,NoDocente,Materia,Oficina

class DocenteForm(forms.ModelForm):

    class Meta:
        """Meta definition for Docenteform."""
        model = Docente
        fields = (
        'last_name',
        'first_name',
        'age',
        'materia',
        'avatar',
        )

class NoDocenteForm(forms.ModelForm):

    class Meta:
        """Meta definition for Docenteform."""
        model = NoDocente
        fields = (
        'last_name',
        'first_name',
        'age',
        'oficina',
        'avatar',
        )

class MateriaForm(forms.ModelForm):

    class Meta:
        """Meta definition for Materiaform."""

        model = Materia
        fields = (
            'name',
            'short_name',
            )

class OficinaForm(forms.ModelForm):

    class Meta:
        """Meta definition for Materiaform."""

        model = Oficina
        fields = (
            'name',
            'short_name',
            )   
