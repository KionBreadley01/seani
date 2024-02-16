from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(
        verbose_name = 'Nombre del Modulo',
          max_length =30)
    decription = models.CharField(
        verbose_name = 'Descripcion del Modulo',
        max_length = 100)
    
    def __str__(self):
        return self.name

       

class Question(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    quiestion_text = models.CharField(
        null = True, blank = True,
        verbose_name ='Texto de la pregunta',
        max_length = 255)
    Question_image = models.ImageField(
        null = True, blank = True,
        verbose_name='Imagen de la pregunta',
        upload_to='question')
    answert1 = models.CharField( 
        verbose_name='Respuesta A',
        max_length = 150)
    answert2 = models.CharField( 
        verbose_name='Respuesta B',
        max_length = 150)
    answert3 = models.CharField(
        null = True, blank = True,
        verbose_name='Respuesta C',
        max_length = 150)
    answert4 = models.CharField(
        null = True, blank = True,
        verbose_name='Respuesta D',
        max_length = 150)
    correct = models.CharField( 
        verbose_name='Respuesta Correacta',
        max_length = 5)

def __str__(self):
    return f"{self.module.name } Pregunta {self.id}"

    class Meta:
        verbose_name ='modulo'
        verbose_name_prural='modulo'

