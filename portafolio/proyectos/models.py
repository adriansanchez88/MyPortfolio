from django.db import models
from ckeditor.fields import RichTextField

def remplazarImagen(instance, filename):    
    if Proyecto.objects.filter(pk=instance.pk).exists():
        old_instance = Proyecto.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
    return 'proyectos/' + filename

def remplazarImagenDeFondo(instance, filename):    
    if Proyecto.objects.filter(pk=instance.pk).exists():
        old_instance = Proyecto.objects.get(pk=instance.pk)
        old_instance.imagenDeFondo.delete()
    return 'proyectos/' + filename

class Proyecto(models.Model):    
    título = models.CharField(max_length=200, verbose_name = 'Título')
    descripción = models.TextField(verbose_name = 'Descripción')
    imagen = models.ImageField(verbose_name = 'Imagen', upload_to = remplazarImagen)
    imagenDeFondo = models.ImageField(verbose_name = 'Imagen de Fondo', upload_to = remplazarImagenDeFondo)
    información = RichTextField(verbose_name= 'Informacion del proyecto', default= '')
    enlace = models.URLField(verbose_name= 'Enlace', null=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')
    modificado = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de modificación')
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-creado']

    def __str__(self):
        return self.título