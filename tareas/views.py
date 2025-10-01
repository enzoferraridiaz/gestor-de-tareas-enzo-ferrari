from django.urls import reverse_lazy
from django.views import generic
from .models import Tarea


class TareaListView(generic.ListView):
    model = Tarea
    paginate_by = 10 # opcional
    template_name = 'tareas/tarea_list.html'
    context_object_name = 'tareas'


class TareaDetailView(generic.DetailView):
    model = Tarea
    template_name = 'tareas/tarea_detail.html'


class TareaCreateView(generic.CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:list')


class TareaUpdateView(generic.UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'prioridad', 'vigente', 'fecha_limite']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:list')


class TareaDeleteView(generic.DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tareas:list')

# tareas/views.py
