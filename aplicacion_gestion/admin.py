from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Columnas que se verán en la tabla principal de Proyectos
    list_display = ('nombre', 'usuario', 'fecha_inicio')
    
    # Buscador por nombre de proyecto o por el nombre del usuario asignado
    search_fields = ('nombre', 'usuario__username')
    
    # Filtros laterales por fecha de inicio
    list_filter = ('fecha_inicio',)


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    # Columnas principales en el listado de Tareas
    list_display = ('titulo', 'proyecto', 'estado', 'fecha_vencimiento')
    
    # Filtros laterales por estado de la tarea y fecha de vencimiento
    list_filter = ('estado', 'fecha_vencimiento', 'proyecto')
    
    # Buscador por título de la tarea o por nombre del proyecto
    search_fields = ('titulo', 'proyecto__nombre')
    
    # Permite cambiar el estado de la tarea directamente desde la lista, sin entrar a editarla toda
    list_editable = ('estado',)