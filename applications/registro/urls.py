from django.contrib import admin
from django.urls import path, include
from . import views

app_name='registro_app'

urlpatterns = [
    path('listar-docente/',views.DocenteListViewAll.as_view(), name='listar-docente'),
    path('listar-nodocente/',views.NoDocenteListViewAll.as_view(), name='listar-nodocente'),
    path('listar-por-materia/<short_name>/',views.DocenteListViewPorAsignatura.as_view(), name='listar-por-materia'),
    path('detalle-docente/<pk>/',views.DocenteDetailView.as_view(), name='detalle-docente'),
    path('detalle-nodocente/<pk>/',views.NoDocenteDetailView.as_view(), name='detalle-nodocente'),
    path('listar-por-oficina/<short_name>/',views.NoDocenteListViewPorOficina.as_view(), name='listar-por-oficina'),
    path('buscar-por-apellido/',views.DocenteListViewBuscar.as_view(), name='buscar-por-apellido'),
    path("buscar-nodocente-por-apellido/",views.NoDocenteListViewBuscar.as_view(), name="buscar-nodocente"),
    path("exito/",views.SuccessView.as_view(), name="exito"),
    path("alta-docente/",views.DocenteCreateView.as_view(), name="alta-docente"),
    path('alta-nodocente/',views.NoDocenteCreateView.as_view(), name='alta-nodocente'),
    path('update-docente/<pk>',views.DocenteUpdateView.as_view(), name='update-docente'),
    path('update-nodocente/<pk>', views.NoDocenteUpdateView.as_view(), name='update-nodocente'),
    path('delete-docente/<pk>', views.DocenteDeleteView.as_view(), name='delete-docente'),
    path('delete-nodocente/<pk>',views.NoDocenteDeleteView.as_view(), name='delete-nodocente'),
    path('listar-materia/', views.MateriaListViewAll.as_view(), name='listar-materia'),
    path('listar-oficina/', views.OficinaListViewAll.as_view(), name='listar-oficina'),
    path('', views.VistaPrincipal.as_view(), name='index'),
    path('detalle-materia/<pk>', views.MateriaDetailView.as_view(), name='detalle-materia'),
    path('buscar-materia/', views.MateriaListViewBuscar.as_view(), name='buscar-materia'),
    path('alta-materia/', views.MateriaCreateView.as_view(), name='alta-materia'),
    path('update-materia/<pk>', views.MateriaUpdateView.as_view(), name='update-materia'),
    path('delete-materia/<pk>', views.MateriaDeleteView.as_view(), name='delete-materia'),
    path('detalle-oficina/<pk>', views.OficinaDetailView.as_view(), name='detalle-oficina'),
    path('buscar-oficina/', views.OficinaListViewBuscar.as_view(), name='buscar-oficina'),
    path('alta-oficina/', views.OficinaCreateView.as_view(), name='alta-oficina'),
    path('update-oficina/<pk>', views.OficinaUpdateView.as_view(), name='update-oficina'),
    path('delete-oficina/<pk>', views.OficinaDeleteView.as_view(), name='delete-oficina'),
    
]
