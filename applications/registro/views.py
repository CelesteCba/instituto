from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Docente,NoDocente,Materia,Oficina
from .forms import DocenteForm,NoDocenteForm,MateriaForm,OficinaForm


# Create your views here.
class DocenteListViewAll(ListView):
    model = Docente
    template_name = "registro/list_all_docente.html"
    ordering = 'last_name'
    context_object_name = 'lista_docente'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = Docente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

class MateriaListViewAll(ListView):
    model = Materia
    template_name = "registro/list_all_materia.html"
    ordering = 'name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = Materia.objects.filter(
            name__icontains = palabra_clave
        )
        return lista

class OficinaListViewAll(ListView):
    model = Oficina
    template_name = "registro/list_all_oficina.html"
    ordering = 'name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = Oficina.objects.filter(
            name__icontains = palabra_clave
        )
        return lista


class NoDocenteListViewAll(ListView):
    model = NoDocente
    template_name = "registro/list_all_nodocente.html"
    ordering= 'last_name'
    context_object_name = 'lista_nodocente'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = NoDocente.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

class DocenteListViewPorAsignatura(ListView):
    model = Docente
    template_name = "registro/listar_por_materia.html"
    context_object_name = 'lista'

    def get_queryset(self):
        asignatura = self.kwargs['short_name']
        lista = Docente.objects.filter(
            materia__short_name= asignatura
        )
        return lista

class NoDocenteListViewPorOficina(ListView):
    model = Docente
    template_name = "registro/listar_por_oficina.html"
    context_object_name = 'lista'

    def get_queryset(self):
        oficina = self.kwargs['short_name']
        lista = NoDocente.objects.filter(
            oficina__short_name= oficina
        )
        return lista

class DocenteDetailView(DetailView):
    model = Docente
    template_name = "registro/detalle_docente.html"
    context_object_name = 'detalle_docente'


class NoDocenteDetailView(DetailView):
    model = NoDocente
    template_name = "registro/detalle_nodocente.html"
    context_object_name = 'detalle_nodocente'


class MateriaDetailView(DetailView):
    model = Materia
    template_name = "registro/detalle_materia.html"
    context_object_name = 'detalle_materia'

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = "registro/detalle_oficina.html"
    context_object_name = 'detalle_oficina'


class DocenteListViewBuscar(ListView):
    model = Docente
    template_name = "registro/buscar_docente.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = Docente.objects.filter(
            last_name = palabra_clave
        )
        return lista

class MateriaListViewBuscar(ListView):
    model = Materia
    template_name = "registro/buscar_materia.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = Materia.objects.filter(
            name = palabra_clave
        )
        return lista
 
class OficinaListViewBuscar(ListView):
    model = Materia
    template_name = "registro/buscar_oficina.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = Oficina.objects.filter(
            name = palabra_clave
        )
        return lista

class NoDocenteListViewBuscar(ListView):
    model = NoDocente
    template_name = "registro/buscar_nodocente.html"
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword','')
        lista = NoDocente.objects.filter(
            last_name = palabra_clave
        )
        return lista



class SuccessView(TemplateView):
    template_name = "registro/exito.html"

class DocenteCreateView(CreateView):
    model = Docente
    template_name = "registro/alta_docente.html"
    form_class = DocenteForm
    success_url = reverse_lazy('registro_app:listar-docente')


class NoDocenteCreateView(CreateView):
    model = NoDocente
    template_name = "registro/alta_nodocente.html"
    form_class = NoDocenteForm
    success_url = reverse_lazy('registro_app:listar-nodocente')


class MateriaCreateView(CreateView):
    model = Materia
    template_name = "registro/alta_materia.html"
    form_class = MateriaForm
    success_url = reverse_lazy('registro_app:listar-materia')

class OficinaCreateView(CreateView):
    model = Oficina
    template_name = "registro/alta_oficina.html"
    form_class = OficinaForm
    success_url = reverse_lazy('registro_app:listar-oficina')
  
 

class DocenteUpdateView(UpdateView):
    model = Docente
    template_name = "registro/update_docente.html"
    form_class = DocenteForm
    success_url = reverse_lazy('registro_app:listar-docente')


class NoDocenteUpdateView(UpdateView):
    model = NoDocente
    template_name = "registro/update_nodocente.html"
    form_class = NoDocenteForm
    success_url = reverse_lazy('registro_app:listar-nodocente')


class MateriaUpdateView(UpdateView):
    model = Materia
    template_name = "registro/update_materia.html"
    form_class = MateriaForm
    success_url = reverse_lazy('registro_app:listar-materia')

class OficinaUpdateView(UpdateView):
    model = Oficina
    template_name = "registro/update_oficina.html"
    form_class = OficinaForm
    success_url = reverse_lazy('registro_app:listar-oficina')

class DocenteDeleteView(DeleteView):
    model = Docente
    template_name = "registro/delete_docente.html"
    success_url = reverse_lazy('registro_app:listar-docente')

class NoDocenteDeleteView(DeleteView):
    model = NoDocente
    template_name = "registro/delete_nodocente.html"
    success_url = reverse_lazy('registro_app:listar-nodocente')

class MateriaDeleteView(DeleteView):
    model = Materia
    template_name = "registro/delete_materia.html"
    success_url = reverse_lazy('registro_app:listar-materia')

class OficinaDeleteView(DeleteView):
    model = Oficina
    template_name = "registro/delete_oficina.html"
    success_url = reverse_lazy('registro_app:listar-oficina')


class VistaPrincipal(TemplateView):
    template_name = "index.html"



