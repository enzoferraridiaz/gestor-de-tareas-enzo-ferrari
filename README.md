# Abrir shell
python manage.py shell


from tareas.models import Tarea
from django.utils import timezone


# Crear
Tarea.objects.create(titulo='Pagar factura', descripcion='Pagar factura luz', prioridad=2, vigente=True)


# Listar
Tarea.objects.all()


# Filtrar por prioridad alta (1 o 2)
Tarea.objects.filter(prioridad__lte=2).order_by('prioridad')


# Obtener una tarea, editar y guardar
t = Tarea.objects.get(pk=1)
t.vigente = False
t.save()


# Borrar
Tarea.objects.filter(vigente=False).delete()


# Conteo
Tarea.objects.count()


# Tareas con fecha límite pasada
Tarea.objects.filter(fecha_limite__lt=timezone.now().date())
