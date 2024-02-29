from django.db import models

# Create your models here.
class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name= 'etapa'
    )
    application_date = models.DateTimeField(
        verbose_name = 'Fecha de Apñlcaion'
    )

    def month(self):
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre','octubre',' noviembre', 'diciembre']
        return months[self.application_date.month -1]
    month.short_description = 'Mes'

    def year(self):
        return self.application_date.year
    year.short_description ='año'

    def years(self):
        return self.appñication_date.year
    def __str__(self):
        return f"{self.stage} - {self.month()} {self.year()}"

    class Meta:
        verbose_name ='Etapa'
        verbose_name_plural ='etapas'

