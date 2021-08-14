from django.db import models

# Create your models here.
class BlogPost(models.Model):
    tittle=models.CharField(max_length=200,verbose_name="titulo")
    content=models.TextField(verbose_name="contenido del post")
    created=models.DateTimeField(null=True, blank=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(null=True,blank=True,verbose_name="Fecha de actualización")
    image=models.ImageField(verbose_name="imagen")#,, height_field=None, width_field=None, max_length=1
    
    
    def __str__(self):
        return self.tittle