from django.urls import path
from .views import HomeView, ProyectoCreateView, TareaCreateView, TareaDeleteView, TareaUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('proyecto/nuevo/', ProyectoCreateView.as_view(), name='crear_proyecto'),
    path('proyecto/<int:proyecto_id>/tarea/nueva/', TareaCreateView.as_view(), name='crear_tarea'),
    path('tarea/<int:pk>/editar/', TareaUpdateView.as_view(), name='editar_tarea'),  # <-- Nueva ruta
    path('tarea/<int:pk>/eliminar/', TareaDeleteView.as_view(), name='eliminar_tarea'),  # <-- Nueva ruta
]