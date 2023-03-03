from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
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