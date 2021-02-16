from .models import Proyecto
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ProyectoListView(ListView):
    model = Proyecto
    paginate_by = 3

class ProyectoDetailView(DetailView):
    model = Proyecto