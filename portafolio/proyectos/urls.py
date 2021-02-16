from django.urls import path
from .views import ProyectoListView, ProyectoDetailView

proyectos_patterns = ([
    path('', ProyectoListView.as_view(), name='list'),
    path('<int:pk>/<slug:slug>/', ProyectoDetailView.as_view(), name='detail'),
], 'proyectos')