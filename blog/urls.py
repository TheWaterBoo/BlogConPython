#blog/urls
from django.urls import path 
from .views import VistaListaBlog, VistaDetalleBlog, VistaCreacionPublicacionBlog, VistaModificacionBlog, VistaEliminarPublicacion

urlpatterns = [
    path ('', VistaListaBlog.as_view(), name= 'inicio'),
    path ('pub/<int:pk>/', VistaDetalleBlog.as_view(), name = 'detalle_pub'),
    path ('pub/nueva/', VistaCreacionPublicacionBlog.as_view(), name='publicacion_nueva'),
    path ('pub/<int:pk>/editar/', VistaModificacionBlog.as_view(), name='editar_publicacion'),
    path ('pub/<int:pk>/eliminar/', VistaEliminarPublicacion.as_view(), name='eliminar_publicacion'),
]   
