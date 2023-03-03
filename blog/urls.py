#blog/urls
from django.urls import path 
from .views import VistaListaBlog, VistaDetalleBlog, VistaCreacionPublicacionBlog

urlpatterns = [
    path ('', VistaListaBlog.as_view(), name= 'inicio'),
    path ('pub/<int:pk>/', VistaDetalleBlog.as_view(), name = 'detalle_pub'),
    path('pub/nueva/', VistaCreacionPublicacionBlog.as_view(), name='publicacion_nueva'),
]   
