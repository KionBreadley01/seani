# Generated by Django 5.0.2 on 2024-02-22 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(verbose_name='etapa')),
                ('application_date', models.DateTimeField(verbose_name='Fecha de Apñlcaion')),
            ],
        ),
    ]
