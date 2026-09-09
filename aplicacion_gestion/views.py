from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proyecto, Tarea
from .forms import ProyectoForm, TareaForm

 

class HomeView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'aplicacion_gestion/home.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)

class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'aplicacion_gestion/proyecto_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Asigna automáticamente el usuario logueado al proyecto
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'aplicacion_gestion/tarea_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Asigna la tarea al proyecto correspondiente enviado por URL
        proyecto_id = self.kwargs['proyecto_id']
        form.instance.proyecto = get_object_or_404(Proyecto, id=proyecto_id, usuario=self.request.user)
        return super().form_valid(form)

class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'aplicacion_gestion/tarea_form.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        # Asegura que el usuario solo pueda editar tareas de sus propios proyectos
        return Tarea.objects.filter(proyecto__usuario=self.request.user)

class TareaDeleteView(LoginRequiredMixin, DeleteView):
     model = Tarea
     template_name = 'aplicacion_gestion/tarea_confirm_delete.html'
     success_url = reverse_lazy('home')

     def get_queryset(self):
        return Tarea.objects.filter(proyecto__usuario=self.request.user)