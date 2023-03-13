from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Publicacion

# Create your views here.
class VistaListaBlog(ListView):
  model = Publicacion 
  template_name = 'inicio.html'
    
class VistaDetalleBlog(DetailView):
  model = Publicacion
  template_name = 'detalle_pub.html'

class VistaCreacionPublicacionBlog(CreateView):
  model = Publicacion
  template_name = 'publicacion_nueva.html'
  fields = ['titulo', 'autor', 'cuerpo']

class VistaModificacionBlog(UpdateView):
  model = Publicacion
  template_name = 'editar_publicacion.html'
  fields = ['titulo','cuerpo']

class VistaEliminarPublicacion(DeleteView):
  model = Publicacion
  template_name = 'eliminar_publicacion.html'
  success_url = reverse_lazy('inicio')