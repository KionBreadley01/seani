from django.db import models

# Create your models here.
class Career(models.Model):
    Levels=[
        ('TSU','Tecnivo Superior Universitario'),
        ('Ing','Ingeneria'),
        ('Lic','Licenciatura'),
        ('M','Maestria')
    ]
    level = models.CharField(
        verbose_name ='Nivel',
        max_length = 150,
        choices = Levels
    )

    name= models.CharField(
        verbose_name = 'Nombre',
        max_length = 150
    )
    short_name = models.CharField(
        verbose_name='Abrebiatura',
        max_length = 20

    )
    short_name = models.CharField(
        verbose_name='Abrebiatura',
        max_length = 20
    )
    def __str__(self) -> str:
        return f"{self.level}{self.short_name}"
    
    class Meta:
        verbose_name ='carrera'
        verbose_name_plural ='carreras'
   
             
