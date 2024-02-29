from django.contrib import admin

# Register your models here.

from .models import Stage

@admin.register(Stage)
class stageAdmin(admin.ModelAdmin):
    list_display = ['stage', 'month','years']

