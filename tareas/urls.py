from django.urls import path
from . import views
app_name = 'tareas'
urlpatterns = [
    path('', views.TareaListView.as_view(), name='list'),
    path('tarea/<int:pk>/', views.TareaDetailView.as_view(), name='detail'),
    path('tarea/nueva/', views.TareaCreateView.as_view(), name='create'),
    path('tarea/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='update'),
    path('tarea/<int:pk>/borrar/', views.TareaDeleteView.as_view(), name='delete'),
]